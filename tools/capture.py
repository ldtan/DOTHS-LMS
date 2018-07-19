# [START of Imports]
import config
import cv2
import numpy as np
import os
# [END of Imports]

"""
Function used to capture an image.

Press 'spacebar' to take a picture.
Press 'esc' to exit the function.

Args:
    save_after (bool): 
    device_index (int): 
    save_to (str): 
    image_name (str): 
    image_format (str): 

Returns:
    tuple: (
        numpy.ndarray: Image captured.
        str: Path of the saved image.
    )
    If `save_after` is True, else
    numpy.ndarray: Image captured.
"""
def capture_image(save_after=False, device_index=config.DEFAULT_DEVICE_INDEX,
        save_to=config.APP_FILES_PATH, image_name=config.DEFAULT_IMAGE_NAME,
        image_format=config.DEFAULT_IMAGE_FORMAT):

    camera = cv2.VideoCapture(device_index)
    cv2.namedWindow('Image Capture')

    image_captured = None
    path = None

    while True:
        _, frame = camera.read()

        if not _:
            break

        cv2.imshow('Image Capture', frame)
        key = cv2.waitKey(1)

        # Pressed 'esc' button.
        if key == 27:
            break

        # Pressed 'spacebar' button.
        elif key == 32:
            if not os.path.exists(save_to):
                os.makedirs(save_to)

            image_captured = frame
            path = os.path.join(save_to, '{}{}'.format(image_name, image_format))
            cv2.imwrite(path, image_captured)

            break

    camera.release()
    cv2.destroyAllWindows()
    
    return (image_captured, path) if save_after else image_captured


"""
Function used to capture a stream of images.

Press 'spacebar' to start taking images per frame, then press again to stop.
Press 'esc' to exit the function.

Args:
    device_index (int): 
    image_limit (int): 
    time_limit (int): 
    save_to (str): 
    directory_name (str): 
    image_format (str): 

Returns:
    tuple: (
        list: Stream of captured images.
        list: Paths of the saved images.
    )
    If `save_after` is True, else
    list: Stream of captured images.
"""
def capture_image_stream(save_after=False,
        device_index=config.DEFAULT_DEVICE_INDEX,
        image_limit=None, time_limit=None,
        save_to=config.APP_FILES_PATH,
        directory_name=config.DEFAULT_IMAGE_NAME,
        image_format=config.DEFAULT_IMAGE_FORMAT):

    camera = cv2.VideoCapture(device_index)
    cv2.namedWindow('Image Capture')
    on_capture = False
    path = os.path.join(save_to, directory_name)
    image_stream = []
    image_paths = []

    while True:
        _, frame = camera.read()

        if not _:
            break

        cv2.imshow('Image Capture', frame)
        key = cv2.waitKey(1)

        # Pressed 'esc' button.
        if key == 27:
            break

        # Pressed 'spacebar' button.
        elif key == 32:
            if not on_capture:
                on_capture = True

            else:
                break

        if save_after and not os.path.exists(path):
            os.makedirs(path)

        image_count = len(image_stream)

        if on_capture:
            image_path = os.path.join(path, '{}-{}{}'.format(
                    directory_name, str(image_count + 1).zfill(10),
                    image_format))

            if save_after:
                cv2.imwrite(image_path, frame)

            image_stream.append(frame)
            image_paths.append(image_path)

        if image_count >= image_limit:
            break

    camera.release()
    cv2.destroyAllWindows()

    return (image_stream, image_paths) if save_after else image_stream


"""
Function used to record a video.

Press 'spacebar' to start recording, then press again to stop.
Press 'esc' to exit the function.

Args:
    device_index (int): 
    time_limit (int): 
    save_to (str): 

Returns:
    str: Path of the saved video.
"""
def capture_video(device_index=config.DEFAULT_DEVICE_INDEX, time_limit=None,
        save_to=config.APP_FILES_PATH):
    pass


# print capture_image(image_name='sample')
# print capture_image_stream(directory_name='sample', save_after=True)
