from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2
import requests
import time
import argparse
import time

URL_EDUCATIONAL = "http://things.ubidots.com"
URL_INDUSTRIAL = "http://industrial.api.ubidots.com"
INDUSTRIAL_USER = True  # Set this to False if you are an educational user
TOKEN = "...."  # Put here your Ubidots TOKEN
DEVICE = "detector"  # Device where will be stored the result
VARIABLE = "people"  # Variable where will be stored the result

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detector(image):
    '''
    @image is a numpy array
    '''

    clone = image.copy()

    (rects, weights) = HOGCV.detectMultiScale(image, winStride=(4, 4),
                                              padding=(8, 8), scale=1.05)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(clone, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Applies non-max supression from imutils package to kick-off overlapped
    # boxes
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    result = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    return result

def localDetect(image):
    result = []
    flag = False
    image = imutils.resize(image, width=min(400, image.shape[1]))
    clone = image.copy()
    if len(image) <= 0:
        print("[ERROR] could not read your local image")
        return result
#    print("[INFO] Detecting people")
    result = detector(image)
   
    for (xA, yA, xB, yB) in result:
        flag = True
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    cv2.imwrite("result.png", np.hstack((clone, image)))
    return flag


def detectPeople(image):
#    print("[INFO] Image path provided, attempting to read image")
    flag = localDetect(image)
#    print("[INFO] sending results")
    return flag
