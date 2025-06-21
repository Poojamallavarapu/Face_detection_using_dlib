import cv2
import face_recognition
import numpy as np
import os
import uuid

# Folder to store saved faces
os.makedirs("unique_faces", exist_ok=True)

# Store average encoding per unique person
known_face_averages = []
person_count = 0

# Start webcam
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("❌ Error: Webcam could not be opened.")
    exit()

print("✅ Webcam started. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Ensure valid frame
    if rgb_small_frame is None or rgb_small_frame.dtype != np.uint8:
        continue

    # Face detection and encoding
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        is_new_face = True

        # Compare with average encodings of known faces
        for avg_encoding in known_face_averages:
            distance = np.linalg.norm(avg_encoding - face_encoding)
            if distance < 0.38:  # 💡 Tuned threshold to reduce false duplicates
                is_new_face = False
                break

        if is_new_face:
            known_face_averages.append(face_encoding)
            person_count += 1

            # Scale back coordinates to original frame size
            top, right, bottom, left = [coord * 4 for coord in face_location]

            # Crop and save the unique face
            face_image = frame[top:bottom, left:right]
            unique_filename = f"unique_faces/Person_{person_count}_{uuid.uuid4().hex[:6]}.jpg"
            cv2.imwrite(unique_filename, face_image)
            print(f"🆕 New unique face saved: {unique_filename}")

        # Draw rectangle around the face
        top, right, bottom, left = [coord * 4 for coord in face_location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Show live video
    cv2.imshow("Unique Face Detector", frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
