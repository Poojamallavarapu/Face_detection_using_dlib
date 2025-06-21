FACE DETECTION USING DLIB

Python version - 3.10.9

Numpy version - 1.26.4

Download dlib from pip install "https://raw.githubusercontent.com/Cool-PY/Python-Dlib-Repository/main/dlib-19.22.99-cp310-cp310-win_amd64.whl"

install cmake

errors encountered : dlib issues and Unsupported image type, must be 8bit gray or RGB image. Resolved by downgrading the numpy and python versions to above mentioned and dlib downloaded from the above github. 

This is a face detection model , since created with dlib it ensures different faces to be saved  and can even return same faces as different persons in different angles . This model is a very basic model . For improved results the model need to be pretained with large amount of datasets . 

CODES USED IN TERMINAL 

1. python -m venv venv310
.\venv310\Scripts\activate


2. pip install numpy==1.26.4
pip install opencv-python
pip install face_recognition


3. pip install "https://raw.githubusercontent.com/Cool-PY/Python-Dlib-Repository/main/dlib-19.22.99-cp310-cp310-win_amd64.whl"

4. pip install pillow click face-recognition-models

5 .unique_face_detector.py


6. python unique_face_detector.py


7. To clone your project in github:
  git init
  git add .
  git commit -m "Initial commit"
  git remote add origin https://github.com/your-username/your-repo-name.git
  git push -u origin main
 

8. If .git/index.lock error occurred:
   del .git\index.lock




