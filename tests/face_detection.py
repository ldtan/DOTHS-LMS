# [START of Imports]
import cv2
from tools.capture import capture
from tools.image_processing.face import detect_face, detect_faces
# [END of Imports]

def detect_faces_in_frame(frame, seen_frame):
    detected = detect_faces(frame)

    if detected == None:
        return None

    for _, bounds in detect_faces(frame):
        (x, y, w, h) = bounds
        cv2.rectangle(seen_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)


capture(listeners=[detect_faces_in_frame])
