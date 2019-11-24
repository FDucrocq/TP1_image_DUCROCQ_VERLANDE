# library imports
import cv2.cv2 as cv

# load an image
b1 = cv.imread('../../images/moto.jpg')
b2 = cv.imread('../../images/dolphin.jpg')

# load an image as a single channel grayscale
if b1.shape[:2] == b2.shape[:2]:
    sum_img = cv.add(b1, b2) # add images together

    cv.imshow('Summed Images', sum_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    scaled_img = cv.add(b1, 200)

    cv.imshow('Scalar Addition on Dolphin Image', scaled_img)
    cv.waitKey(0)
    cv.destroyAllWindows()