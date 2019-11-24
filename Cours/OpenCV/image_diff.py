# library imports
import cv2.cv2 as cv

# load an image
b1 = cv.imread('../../images/moto.jpg')
b2 = cv.imread('../../images/dolphin.jpg')

# load an image as a single channel grayscale
if b1.shape[:2] == b2.shape[:2]:
    diff = cv.absdiff(b1, b2)  # add images together

    cv.imshow('Summed Images', diff)
    cv.waitKey(0)
    cv.destroyAllWindows()
