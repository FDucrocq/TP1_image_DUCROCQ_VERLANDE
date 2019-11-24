# library imports
import cv2.cv2 as cv

# load an image
dolphin = cv.imread('../images/fruit.jpeg', 0)

# load an image as a single channel grayscale
cv.imshow('Source Image', dolphin)
newImg, th1 = cv.threshold(dolphin, 149, 255, cv.THRESH_BINARY)

cv.imshow('Seuillage', th1)
cv.waitKey(0)
cv.destroyAllWindows()
