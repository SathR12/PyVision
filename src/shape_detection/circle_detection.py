#Vision library for frc robotics
import numpy as np
import cv2 as cv

def isCircle(contour, min_circ_check = .7, max_circ_check = 1.0, max_aspect = 1.1, min_aspect = .8):
    global contour_area, radius, center, x, y, w, h
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    (coord_x, coord_y), radius = cv.minEnclosingCircle(contour)
    center = (int(coord_x), int(coord_y))
    
    contour_area = cv.contourArea(contour) 
    x, y, w, h = cv.boundingRect(contour)
    aspect_ratio = w/h
    new_circle = max_circ_check >= contour_area / (radius**2 * 3.14) >= min_circ_check
    old_circle = (3.14 * cv.minEnclosingCircle(contour)[1] ** 2 - cv.contourArea(contour) < (3.14 * cv.minEnclosingCircle(contour)[1] ** 2) * (1 - 0.69))
    ratio = max_aspect >= aspect_ratio >= min_aspect and contour_area > 700
    if old_circle and new_circle and ratio and len(approx) > 8: 
        return True
    
    return False



    




    