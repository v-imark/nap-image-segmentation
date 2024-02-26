def exclude_small_masks(masks, threshold=0.01):
    """Excludes masks whose size is less than threshold*size of corresponding image."""
    filtered_masks = []
    min_area = masks[0]["crop_box"][2] * masks[0]["crop_box"][3] * threshold
    for mask in masks:
        if mask["area"] >= min_area:
            filtered_masks.append(mask)

    return filtered_masks
