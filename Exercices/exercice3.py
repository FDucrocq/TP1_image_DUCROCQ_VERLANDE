# library imports
import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def compare(img_source, img_reference):
    hist_requete = cv.calcHist([img_requete], [0], None, [256], [0, 256])
    hist_ref = cv.calcHist([img_reference], [0], None, [256], [0, 256])
    current_matching_value = cv.compareHist(hist_requete, hist_ref, cv.HISTCMP_CORREL)
    return current_matching_value


# Chargement d'une image
img_requete = cv.imread('../images/waves.jpg')
cv.imshow("Input", img_requete)

# Variable contenant la meilleur image correspondant à la requête
best_matching_img = None

# Images de référence
img_1 = cv.imread('../images/beach.jpg')
img_2 = cv.imread('../images/dog.jpg')
img_3 = cv.imread('../images/bear.jpg')
img_4 = cv.imread('../images/lake.jpg')
img_5 = cv.imread('../images/moose.jpg')
img_references = [img_1, img_2, img_3, img_4, img_5]

# Calcul de la meilleure image correspondant à la requête
best_matching_value = -1
for reference in img_references:
    value = compare(img_requete, reference)
    if value > best_matching_value:
        best_matching_value = value
        best_matching_img = reference

# Affichage de la meilleure image
cv.imshow("Best Matching Image", best_matching_img)
cv.waitKey(0)
cv.destroyAllWindows()
