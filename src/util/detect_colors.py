import cv2 as cv
import numpy as np

def createMask(image, lower, upper):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, np.array(lower), np.array(upper))
    return mask

def createRes(image, lower, upper):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, np.array(lower), np.array(upper))
    res = cv.bitwise_and(image, image, mask = mask)
    return res

def createDoubleMask(image, lower_1, upper_1, lower_2, upper_2):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask_1 = cv.inRange(hsv, np.array(lower_1), np.array(upper_1))
    mask_2 = cv.inRange(hsv, np.array(lower_2), np.array(upper_2))
    mask = mask_1 + mask_2
    return mask
    
def createDoubleRes(image, lower_1, upper_1, lower_2, upper_2):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask_1 = cv.inRange(hsv, np.array(lower_1), np.array(upper_1))
    mask_2 = cv.inRange(hsv, np.array(lower_2), np.array(upper_2))
    mask = mask_1 + mask_2
    res = cv.bitwise_and(image, image, mask = mask)
    return res

def createOutline(grayscale, param1, param2, param3):
    canny = cv.Canny(grayscale, param1, param2, param3)
    canny = cv.dilate(canny, None, iterations = 1)
    canny = cv.morphologyEx(canny, cv.MORPH_CLOSE, (7,7))
    canny = cv.morphologyEx(canny, cv.MORPH_OPEN, (7,7))
    return canny

