# imports
import cv2.cv2 as cv

# read and display the image as a reference
img = cv.imread('../../images/moose.jpg')
cv.imshow('Moose Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

cropped = img[109:310, 9:160]
cv.imshow('Cropped Image', cropped)
print("press 's' to save the image as cropped_bicycle.png\n")
key = cv.waitKey(0)  # if you are using a 64-bit machine see below
# the above line should be: key = cv2.waitKey(0) & 0xFF
if key == 27:  # wait for the ESC key to exit
    cv.destroyAllWindows()
elif key == ord('s'):  # wait for 's' key to save and exit
    cv.imwrite('../../images/cropped_moose.png', img)
    cv.destroyAllWindows()
# get the size of the cropped image
height, width = cropped.shape[:2]
print('Cropped Width: {}px, Cropped Height: {}px'.format(width, height))
