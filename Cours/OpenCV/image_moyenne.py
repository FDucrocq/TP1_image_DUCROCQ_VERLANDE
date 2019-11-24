# library imports
import cv2.cv2 as cv

# load an image
rouge = cv.imread('../../images/fond_rouge.jpg')
dolphin = cv.imread('../../images/dolphin.jpg')

# load an image as a single channel grayscale
if rouge.shape[:2] == dolphin.shape[:2]:
    print(rouge)
    cv.imshow('Rouge', rouge)
    cv.imshow('Dolphin', dolphin)
    rouge = cv.normalize(rouge, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
    dolphin = cv.normalize(dolphin, None, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
    average_img = rouge / 2 + dolphin / 2
    alt_average_img = cv.add(rouge, dolphin) / 2
    cv.imshow('Averaged Images', average_img)
    cv.imshow('Alt. Averaged Images', alt_average_img)
    cv.waitKey(0)
    cv.destroyAllWindows()
