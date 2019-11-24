# library imports
import cv2.cv2 as cv
import numpy as np

# Chargement d'une image
img = cv.imread('../images/bgr.png')
cv.imshow('Input', img)

# Récupération de la longueur et la largueur
width = img.shape[0]
height = img.shape[1]

# Récupération des canaux de couleurs
blues, greens, reds = cv.split(img)

# display the image with OpenCV imshow()
# cv.imshow('(B)lues', blues)
# cv.imshow('(G)reens', greens)
# cv.imshow('(R)eds ', reds)

# Création d'une matrice vide avec convertion du depth
zero = np.zeros((width, height))
zero = np.uint8(zero)

RG = cv.merge([zero, greens, reds])
BR = cv.merge((blues, zero, reds))
BG = cv.merge((blues, greens, zero))
B = cv.merge((blues, zero, zero))
G = cv.merge((zero, greens, zero))
R = cv.merge((zero, zero, reds))
cv.imshow('R+G', RG)
cv.imshow('R+B', BR)
cv.imshow('B+G', BG)
cv.imshow('B', B)
cv.imshow('G', G)
cv.imshow('R', R)

# OpenCV waitKey() is a required keyboard binding function after imwshow()
cv.waitKey(0)
# destroy all windows command
cv.destroyAllWindows()