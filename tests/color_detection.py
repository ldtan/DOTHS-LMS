# [START of Imports]
import config
import cv2
import numpy as np
from tools.image_processing.color import detect_color
# [END of Imports]

def callback(x):
    pass


camera = cv2.VideoCapture(config.DEFAULT_DEVICE_INDEX)
window_name = 'Color Detection'
cv2.namedWindow(window_name)

ilowH = 0
ihighH = 179
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

cv2.createTrackbar('lowH', window_name, ilowH, 179, callback)
cv2.createTrackbar('highH', window_name, ihighH, 179, callback)

cv2.createTrackbar('lowS', window_name, ilowS, 255, callback)
cv2.createTrackbar('highS', window_name, ihighS, 255, callback)

cv2.createTrackbar('lowV', window_name, ilowV, 255, callback)
cv2.createTrackbar('highV', window_name, ihighV, 255, callback)

while True:
    _, frame = camera.read()

    if not _:
        break

    ilowH = cv2.getTrackbarPos('lowH', window_name)
    ihighH = cv2.getTrackbarPos('highH', window_name)
    ilowS = cv2.getTrackbarPos('lowS', window_name)
    ihighS = cv2.getTrackbarPos('highS', window_name)
    ilowV = cv2.getTrackbarPos('lowV', window_name)
    ihighV = cv2.getTrackbarPos('highV', window_name)

    detected = detect_color(frame, (ilowH, ilowS, ilowV), (ihighH, ihighS, ihighV))

    if detected != None:
        for contour in detected:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)            

    cv2.imshow(window_name, frame)
    key = cv2.waitKey(1)

    # Pressed 'esc' button.
    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
