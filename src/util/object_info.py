import numpy as np
import cv2 as cv
from cv2 import INTER_AREA
import math

#Info of object in image
def getDistance(focal_length, real_width, width_in_frame):
    distance = (real_width * focal_length) / width_in_frame
    return distance

def drawAngle(image, center1, center2):
    x1, y1 = center1
    x2, y2 = center2
    x = x2 - x1
    y = y2 - y1
    distance = math.sqrt((x**2)+(y**2))
    distance = round(distance)
    cv.line(image, center1, center2, (57, 255, 20), 2)
    cv.putText(image, str(distance), center1, cv.FONT_HERSHEY_DUPLEX, 0.5, (57, 255, 20), thickness=2)
    cv.circle(image, center2, radius = 0, color = (57,255,20), thickness = 5)
    cv.line(image, (x2, 0), (x2, (y2 * 2)), color = (57,255,20), thickness = 2)
    if abs(x2-x1) < 10:
        cv.putText(image, "CENTERED", (x2 - 50,((y2 * 2) - 10)), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, color = (0, 0, 255), thickness = 2)  