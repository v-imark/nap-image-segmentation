import sys

import cv2
import matplotlib as mpl

from utils.annotate_image import annotate_image

sys.path.append("../")

import supervision as sv
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


def annotator(img, masks, path, removed2=None, final=None):
    colormap = mpl.colormaps["Set1"]
    colors = sv.ColorPalette(
        [
            sv.Color(int(r * 255), int(g * 255), int(b * 255))
            for r, g, b, _ in colormap(range(3))
        ]
    )
    # colors = sv.ColorPalette([colors.by_idx(mask["class_id"]) for mask in masks])

    return annotate_image(masks, img, path, colors, 0.5)
    # annotated = annotate_image(removed2, annotated, path, orange_colors, 0.5)
    # annotate_image(final, annotated, path, green_colors, 0.5)
