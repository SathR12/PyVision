import numpy as np
import cv2 as cv
from contour_features import getContours, getEdges, drawRect

def isRect(image, contour):
    edges = getEdges(contour)
    if edges == 4 or edges == 5:
        return True
    
    return False
        
    

    