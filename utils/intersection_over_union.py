from copy import copy
import numpy as np


def calculate_iou(mask1, mask2):
    """Computes the intersection over union (IoU) between two binary masks."""
    intersection = np.logical_and(mask1["segmentation"], mask2["segmentation"]).sum()
    if intersection == 0:
        return 0.0
    union = np.logical_or(mask1["segmentation"], mask2["segmentation"]).sum()
    return intersection / union if union != 0 else 0


def exclude_masks_by_iou(masks, threshold):
    """Excludes masks that exceeds IoU threshold"""
    num_masks = len(masks)
    masks_to_keep = copy(masks)
    for i in range(num_masks):
        exclude = None
        for j in range(num_masks):
            if i != j:
                iou = calculate_iou(masks[i], masks[j])
                if iou >= threshold:
                    exclude = min(masks[i], masks[j], key=lambda k: k["area"])
                    break

        if exclude:
            # masks_to_keep.remove(exclude)
            masks_to_keep = [m for m in masks_to_keep if m["name"] != exclude["name"]]

    return masks_to_keep


def calculate_iou_for_all(masks, mask_metadata):
    for i in range(len(masks)):
        ious = []
        for j in range(len(masks)):
            if i != j:
                iou = calculate_iou(masks[i], masks[j])
                if iou > 0:
                    ious.append({"name": mask_metadata[j]["name"], "iou": iou})
        mask_metadata[i]["ious"] = ious
