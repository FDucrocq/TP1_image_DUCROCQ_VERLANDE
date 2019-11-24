# library imports
import cv2.cv2 as cv

# Saving an Image on a key press
img = cv.imread('../images/image_test.jpg')
cv.imshow('Option to Save image', img)
print("press 's' to save the image as 'image_test_2.jpg\n")
key = cv.waitKey(0)  # NOTE: if you are using a 64-bit machine,this needs to be: key = cv2.waitKey(0) & 0xFF

if key == 27:  # wait for the ESC key to exit
    cv.destroyAllWindows()
elif key == ord('s'):  # wait for 's' key to save and exit
    cv.imwrite('../images/image_test_2.jpg', img)
    cv.destroyAllWindows()

# write an image with imwrite
image_to_save = '../images/image_test_3.jpg'
cv.imwrite(image_to_save, img)

print('Image saved as {}'.format(image_to_save))
