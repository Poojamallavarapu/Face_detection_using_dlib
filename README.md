FACE DETECTION USING DLIB

Python version - 3.10.9

Numpy version - 1.26.4

Download dlib from pip install "https://raw.githubusercontent.com/Cool-PY/Python-Dlib-Repository/main/dlib-19.22.99-cp310-cp310-win_amd64.whl"

install cmake

errors encountered : dlib issues and Unsupported image type, must be 8bit gray or RGB image. Resolved by downgrading the numpy and python versions to above mentioned and dlib downloaded from the above github. 

This is a face detection model , since created with dlib it ensures different faces to be saved  and can even return same faces as different persons in different angles . This model is a very basic model . For improved results the model need to be pretained with large amount of datasets . 
