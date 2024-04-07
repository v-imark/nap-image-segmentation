import os
from pathlib import Path

import cv2
import numpy as np

import sys

sys.path.append("../")

from utils.exclude_small_masks import exclude_small_masks
from utils.intersection_over_union import exclude_masks_by_iou


def read_masks(path, mask_metadata):
    os.chdir(Path(path))
    masks = []
    for i, _ in enumerate(mask_metadata):
        mask = mask_metadata[i]
        img = cv2.imread(mask["name"], cv2.IMREAD_GRAYSCALE)
        _, mask["segmentation"] = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
        mask["segmentation"] = np.array(mask["segmentation"], dtype=bool)
        masks.append(mask)

    return masks


def was_removed(list, x):
    for item in list:
        if item["name"] == x["name"]:
            return False

    return True


def filter_and_edit_json(metadata, min_area, threshold):
    path = Path(Path("./").absolute().parent, metadata["masks"][0]["path"])
    print(path)
    masks = read_masks(path, metadata["masks"])
    after_min_area = exclude_small_masks(masks, min_area)
    after_iou = exclude_masks_by_iou(after_min_area, threshold)
    removed_by_min_area = []
    removed_by_iou = []

    new_metadata = metadata
    for i, mask in enumerate(new_metadata["masks"]):
        new_metadata["masks"][i]["class_id"] = 2
        print(
            "min area:",
            new_metadata["masks"][i]["crop_box"][2]
            * new_metadata["masks"][i]["crop_box"][3]
            * min_area,
        )

        if was_removed(after_iou, mask):
            new_metadata["masks"][i]["class_id"] = 1
            print(mask["area"])
            removed_by_iou.append(masks[i])

        if was_removed(after_min_area, mask):
            new_metadata["masks"][i]["class_id"] = 0
            removed_by_min_area.append(masks[i])

    new_metadata["segmentation_info"]["after_min_area_filter"] = len(after_min_area)
    new_metadata["segmentation_info"]["after_iou_filter"] = len(after_iou)

    print(new_metadata["segmentation_info"])
    print(len(removed_by_min_area))

    return new_metadata, removed_by_min_area, removed_by_iou, after_iou
