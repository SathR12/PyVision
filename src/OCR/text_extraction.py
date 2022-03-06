from PIL import Image
import pytesseract
from pytesseract import Output
import cv2 as cv
import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
def setPath(path):
    pytesseract.pytesseract.tesseract_cmd = path
    
def extractText(img):
    return pytesseract.image_to_string(img)
    

def extractDigits(img):
    return (pytesseract.image_to_string(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))

def detectText(img):
    data = pytesseract.image_to_data(img, output_type = Output.DICT)
    dimensions = len(data['level'])
    for i in range(dimensions):
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
def detectDigits(img):
    data = pytesseract.image_to_data(img, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789', output_type = Output.DICT)
    dimensions = len(data['level'])
    for i in range(dimensions):
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


