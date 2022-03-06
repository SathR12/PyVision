import cv2 as cv
import numpy as np

def detectApples(img):
    image = img
    def getContours(mask):
        global contours
        contours = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        if len(contours) == 2:
            contours = contours[0]
            
        else:
            contours = contours[1]
        
        return contours 

    def isCircle(img, contour):
        approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
        
        (coord_x, coord_y), radius = cv.minEnclosingCircle(contour)
        center = (int(coord_x), int(coord_y))
        
        contour_area = cv.contourArea(contour) 
        x, y, w, h = cv.boundingRect(contour)
        aspect_ratio = w/h
          
        if  1.0 >= contour_area / (radius**2 * 3.14) >= .5 and 1.1 >= aspect_ratio >= .8 and contour_area > 700:
              x,y,w,h = cv.boundingRect(contour)
              aspect_ratio = float(w)/h
              area = float(w*h)
              if .8 <= aspect_ratio <= 1.3 and area > 1000:
                  cv.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
        
        



    def createRedMask(img):
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower = np.array([0,120,70])
        upper = np.array([180,255,255])
        mask0 = cv.inRange(hsv, lower, upper)

        #join masks
        lower = np.array([170,120,70])
        upper = np.array([180,255,255])
        mask1 = cv.inRange(hsv, lower, upper)

        #join
        mask = mask0 + mask1
        return mask

    contours = getContours(createRedMask(image))
    for contour in contours:
        isCircle(image, contour)


