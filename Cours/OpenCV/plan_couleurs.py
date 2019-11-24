# imports
import cv2.cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import gridspec

# read and display the image as a reference
img = cv.imread('../images/dolphin.jpg')
cv.imshow('Moose Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

# Puisque l'image chargée est en couleur, sa taille est de 3 chiffres : # height (# of rows), width (# de cols) et
# enfin des plans de couleur (BGR)
height, width, channels = img.shape[:3]
print('Image height: {}, Width: {}, # of channels: {}'.format(height, width, channels))

# Rappelez-vous que openCV lit comme mode BGR, donc le canal 0 est bleu, le canal
# 1 est vert et le canal 2 est rouge
blues = img[:, :, 0]
greens = img[:, :, 1]
reds = img[:, :, 2]

cv.imshow('Dolphin Blues', blues)
cv.imshow('Dolphin Greens', greens)
cv.imshow('Dolphin Reds', reds)
cv.waitKey(0)
cv.destroyAllWindows()


# Tracer les valeurs pour chaque plan de couleur sur une ligne spécifique :
# plot values for each color plane on a specific row
fig = plt.figure(figsize=(10, 4))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])

# original image
ax0 = plt.subplot(gs[0])
ax0.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # need to convert BGRto RGB
ax0.axhline(50, color='black')  # show the row being used
ax0.axvline(100, color='k'), ax0.axvline(225, color='k')  # ref lines

# image slice
ax1 = plt.subplot(gs[1])
ax1.plot(blues[49, :], color='blue')
ax1.plot(greens[49, :], color='green')
ax1.plot(reds[49, :], color='red')
ax1.axvline(100, color='k', linewidth=2), ax1.axvline(225, color='k', linewidth=2)
plt.suptitle('Examen des valeurs du plan de couleur pour une seule ligne')
plt.show()