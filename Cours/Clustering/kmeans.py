from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2.cv2 as cv
import numpy as np


def centroid_histogram(clt_arg):
    numLabels = np.arange(0, len(np.unique(clt_arg.labels_)) + 1)
    (hist_local, _) = np.histogram(clt_arg.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist_local = hist_local.astype("float")
    hist_local /= hist_local.sum()
    return hist_local


def plot_colors(hist1, centroids):
    local_bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    # loop over the percentage of each cluster and the color of each cluster
    for (percent, color) in zip(hist1, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(local_bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX
    return local_bar


image = cv.imread("../../images/Perruche.png")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

plt.figure()
plt.axis("off")
plt.imshow(image)

image = image.reshape((image.shape[0] * image.shape[1], 3))
clt = KMeans(n_clusters=5)
clt.fit(image)

hist = centroid_histogram(clt)
bar = plot_colors(hist, clt.cluster_centers_)
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

cv.waitKey(0)
