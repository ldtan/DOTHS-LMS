# [START of Imports]
import config
import cv2
import numpy as np
import os
# [END of Imports]

__face_cascade = cv2.CascadeClassifier(os.path.join(config.OPENCV_PATH,
        'build', 'etc', 'lbpcascades', 'lbpcascade_frontalface.xml'))

"""
Function used to detect a face in an image.

Args:
    image (numpy.ndarray): 

Returns:
    tuple: (
        numpy.ndarray: A cropped image of the face detected.
        tuple: (
            int: x-location
            int: y-location
            int: width
            int: height
        )
    )
"""
def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = __face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        return gray[y:y+w, x:x+h], faces[0]

    return None, None


"""
Function used to detect multiple faces.

Args:
    image (numpy.ndarray): 

Returns:
    list: Contain cropped images of faces detected that has the same format as
        function 'detect_face' per list item.
"""
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = __face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    detected = []

    if len(faces) <= 0:
        return None

    for face in faces:
        (x, y, w, h) = face
        detected.append((gray[y:y+w, x:x+h], face))

    return detected


"""
Function used to recognize a face detected from an image.

Args:
    image (numpy.ndarray): 
    faces (list): 
    face_labels (list): 

Returns:
    object: The label representing the face to be the highest match.
"""
def recognize_face(image, faces, face_labels):
    face, _ = detect_face(image)

    if face == None:
        return None

    label_map = {label: len(label_map) + 1 for label in face_labels if label not in label_map}
    labels = [label_map[label] for label in face_labels]

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # face_recognizer = cv2.face.EigenFaceRecognizer_create()
    # face_recognizer = cv2.face.FisherFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))
    label = face_recognizer.predict(face)

    if label == None:
        return None

    for key, value in label_map:
        if value == label:
            return key
