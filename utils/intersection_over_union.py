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
    masks = np.array(masks)
    num_masks = masks.shape[0]
    indices_to_keep = []

    for i in range(num_masks):
        ious = np.array(
            [calculate_iou(masks[i], masks[j]) for j in range(num_masks) if i != j]
        )
        if np.all(ious <= threshold):
            indices_to_keep.append(i)

    filtered_masks = masks[indices_to_keep]
    return filtered_masks.tolist()
