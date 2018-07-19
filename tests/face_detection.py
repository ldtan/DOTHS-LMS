# [START of Imports]
import config
import cv2
import numpy as np
from tools.image_processing.face import detect_face, detect_faces
# [END of Imports]

camera = cv2.VideoCapture(config.DEFAULT_DEVICE_INDEX)
cv2.namedWindow('Image Capture')

while True:
    _, frame = camera.read()

    if not _:
        break

    # _, bounds = detect_face(frame)

    # if isinstance(bounds, np.ndarray):
    #     (x, y, w, h) = bounds
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    detected = detect_faces(frame)

    if detected != None:
        for _, bounds in detected:
            (x, y, w, h) = bounds
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Image Capture', frame)
    key = cv2.waitKey(1)

    # Pressed 'esc' button.
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
