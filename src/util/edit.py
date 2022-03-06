import cv2 as cv

#Image editing
def resizeImage(image, LENGTH, WIDTH):
    image = cv.resize(image, (LENGTH, WIDTH))
    return image

def GaussianBlurImage(image, blur_amount = 7): 
    image = cv.GaussianBlur(image, (blur_amount, blur_amount), 0)
    return image

def MedianBlurImage(image, blur_amount):
    image = cv.medianBlur(image, blur_amount)
    return image

def bilateral2D(image, param1, param2, param3):
    image = cv2.bilateralFilter(image, param1, param2, param3)
    return image
      
def convertRGB(image):
    RGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    return image

def convertGray(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray

def convertHSV(image):
    HSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    return HSV

def dilate_edges(image):
    # dilation to strengthen the edges
    kernel = np.ones((3,3), np.uint8)
    # Creating the kernel for dilation
    dilated_image = cv.dilate(image,kernel,iterations=1)
    return dilated_image

def threshold_OTSU(image):
    # Display Image
    # Thresholding the image
    _, thresh_image = cv.threshold(image, 0, 255, cv.THRESH_OTSU)

    return thresh_image
 
    