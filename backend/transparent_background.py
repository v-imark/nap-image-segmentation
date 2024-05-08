import cv2
import numpy as np


def make_bg_transparent(path):
    na = cv2.imread(str(path))
    # Make a True/False mask of pixels whose BGR values sum to more than zero
    alpha = np.sum(na, axis=-1) > 0

    # Convert True/False to 0/255 and change type to "uint8" to match "na"
    alpha = np.uint8(alpha * 255)

    # Stack new alpha layer with existing image to go from BGR to BGRA, i.e. 3 channels to 4 channels
    res = np.dstack((na, alpha))

    # Save result
    cv2.imwrite(path, res)
