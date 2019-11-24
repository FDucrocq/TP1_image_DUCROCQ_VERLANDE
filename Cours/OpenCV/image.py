# library imports
import cv2.cv2 as cv

# load an image
img = cv.imread('../../images/image_test.jpg')
# load an image as a single channel grayscale
img_single_channel = cv.imread('../../images/dolphin.jpg', cv.IMREAD_GRAYSCALE)
# print some details about the images
print('The shape of img without second arg is: {}'.format(img.shape))
print('The shape of img_single_channel is: {}'.format(img_single_channel.shape))

# display the image with OpenCV imshow()
cv.imshow('Image', img_single_channel)
# OpenCV waitKey() is a required keyboard binding function after imwshow()
cv.waitKey(0)
# destroy all windows command
cv.destroyAllWindows()