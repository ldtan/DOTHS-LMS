# [START of Imports]
import cv2
from tools.capture import capture
from tools.image_processing.color import detect_color
# [END of Imports]

low_h = 0
low_s = 0
low_v = 0
high_h = 179
high_s = 255
high_v = 255

# Blue Range
low_h = 99
low_s = 115
low_v = 150
high_h = 110
high_s = 255
high_v = 255

# Green Range
# low_h = 40
# low_s = 40
# low_v = 40
# high_h = 70
# high_s = 255
# high_v = 255

# Red Range
# low_h = 136
# low_s = 87
# low_v = 111
# high_h = 180
# high_s = 255
# high_v = 255

# Yellow Range
# low_h = 22
# low_s = 60
# low_v = 200
# high_h = 60
# high_s = 255
# high_v = 255

window_name = 'HSV Color Calibration'
cv2.namedWindow(window_name)
callback = lambda x: None

cv2.createTrackbar('Low H', window_name, low_h, 179, callback)
cv2.createTrackbar('Low S', window_name, low_s, 255, callback)
cv2.createTrackbar('Low V', window_name, low_v, 255, callback)

cv2.createTrackbar('High H', window_name, high_h, 179, callback)
cv2.createTrackbar('High S', window_name, high_s, 255, callback)
cv2.createTrackbar('High V', window_name, high_v, 255, callback)


def detect_color_in_frame(frame, seen_frame):
    low_h = cv2.getTrackbarPos('Low H', window_name)
    low_s = cv2.getTrackbarPos('Low S', window_name)
    low_v = cv2.getTrackbarPos('Low V', window_name)
    high_h = cv2.getTrackbarPos('High H', window_name)
    high_s = cv2.getTrackbarPos('High S', window_name)
    high_v = cv2.getTrackbarPos('High V', window_name)
    contours = detect_color(frame, [low_h, low_s, low_v], [high_h, high_s, high_v])

    if contours:
        cv2.drawContours(seen_frame, contours, -1, (0, 255, 0), 3)


capture(listeners=[detect_color_in_frame])
