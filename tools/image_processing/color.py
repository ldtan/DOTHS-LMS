# [START of Imports]
import cv2
import numpy as np
# [END of Imports]

"""
Function used to detect a particular color from an image.

Args:
    image (numpy.ndarray): 
    lower_limit (tuple): 
    higher_limit (tuple): 
    min_dimension (tuple): (
        int: width
        int: height
    )
    max_dimension (tuple): (
        int: width
        int: height
    )

Returns:
    list: Where each item is a tuple containing the accepted_contours detected in the
        image.
"""
def detect_color(image, lower_limit, higher_limit, min_dimension=None,
        max_dimension=None):

    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    # blurred_image = cv2.medianBlur(image, 15)
    # blurred_image = cv2.bilateralFilter(image, 15, 75, 75)

    hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
    lower_limit = np.array(lower_limit)
    higher_limit = np.array(higher_limit)
    mask = cv2.inRange(hsv_image, lower_limit, higher_limit)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
            cv2.CHAIN_APPROX_NONE)
    accepted_contours = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if min_dimension != None:
            if w < min_dimension[0] or h < min_dimension[1]:
                continue

        if max_dimension != None:
            if w > max_dimension[0] or h > max_dimension[1]:
                continue

        accepted_contours.append(contour)

    return accepted_contours if len(accepted_contours) > 0 else None


"""
Function to detect given colors from an image.

Args:
    image (numpy.ndarray): 
    color_limits (dict): 
    min_dimension (tuple): 
    max_dimension (tuple): 

Returns:
    dict: Where each key is a label and the value is a list of tuple containing
        the accepted_contours detected in the image.
"""
def detect_colors(image, color_limits, min_dimension=None, max_dimension=None):
    detected = {}

    for label, limits in color_limits.iteritems():
        accepted_contours = detect_color(image, limits[0], limits[1],
                min_dimension=min_dimension, max_dimension=max_dimension)

        if accepted_contours != None:
            detected.update(label=accepted_contours)

    return detected if len(detected) > 0 else None
