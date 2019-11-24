# library imports
import cv2.cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# CONFIGURATIONS
THRESHOLD = 0.999
SOURCE_IMAGE = "../images/road1.jpg"
TEMPLATE_IMAGE = "../images/stop_sign.png"


# METHODS
def get_match_rate(source, area):
    """" Retrieve a similitude rate between a source image and a template """
    hist_source = cv.calcHist([source], [0], None, [256], [0, 256])
    hist_area = cv.calcHist([area], [0], None, [256], [0, 256])
    return cv.compareHist(hist_source, hist_area, cv.HISTCMP_CORREL)


def main():
    source = cv.imread(SOURCE_IMAGE)
    template = cv.imread(TEMPLATE_IMAGE)

    height, width = template.shape[0:2]

    for i in range(source.shape[0] - height):
        for j in range(source.shape[1] - width):
            area = source[i:i+height, j:j+width]
            if get_match_rate(template, area) >= THRESHOLD:
                cv.imshow("Match", area)
                cv.waitKey(0)


if __name__ == "__main__":
    print("[EXERCICE 4] Début du traitemant")
    main()
    print("[EXERCICE 4] Fin du traitemant")
    cv.destroyAllWindows()
