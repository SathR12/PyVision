import numpy as np
import cv2 as cv

#extract contours
def getContours(mask):
    contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    if len(contours) == 2:
        contours = contours[0]
        
    else:
        contours = contours[1]
    
    return contours

def drawBoundingRect(image, contour, color = (0, 255, 0), thickness = 2):
    min_rect = cv.minAreaRect(contour)
    box = cv.boxPoints(min_rect)
    box = np.int0(box)
    cv.drawContours(image, [box], 0, color, thickness)

def drawRect(image, contour, color = (0, 255, 0), thickness = 2):
    x, y, w, h = cv.boundingRect(contour)
    cv.rectangle(image, (x, y), (x + w, y + h), color, thickness)

def drawCircle(image, contour, color = (0, 255, 0), thickness = 2):
    (coord_x, coord_y), radius = cv.minEnclosingCircle(contour)
    contour_area = cv.contourArea(contour)
    center = (int(coord_x), int(coord_y))
    cv.circle(img, center, int(radius), color, thickness)

def drawAllContours(image, contours, color = (0, 255, 0), thickness = 2):
    cv.drawContours(image, contours, -1, color, thickness)

def getEdges(contour):
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    return len(approx)