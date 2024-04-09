import json
import os
from pathlib import Path

import cv2
import numpy as np


def save_masks(masks, image, img_name, output_path, args, sizes, annotated_path):
    masks_path = Path(output_path, img_name, "masks")
    os.makedirs(masks_path, exist_ok=True)
    json_path = Path(output_path, "metadata.json")
    masks_data = []

    for count, mask in enumerate(masks):
        masked_img = cv2.bitwise_and(
            image, image, mask=mask["segmentation"].astype(np.uint8)
        )
        mask_name = f"{img_name}_mask_{count}.png"
        cv2.imwrite(str(Path(masks_path, mask_name)), masked_img)

        mask_data = {
            "name": mask_name,
            "path": str(masks_path),
            "area": mask["area"],
            "predicted_iou": mask["predicted_iou"],
            "stability_score": mask["stability_score"],
            "crop_box": mask["crop_box"],
            "bbox": mask["bbox"],
            "point_coords": mask["point_coords"],
            "class_id": 2,
        }
        masks_data.append(mask_data)

    json_entry = {
        "name": img_name,
        "dataset": args.dataset,
        "split": args.split,
        "params": {
            "points_per_side": args.points_per_side,
            "points_per_batch": args.points_per_batch,
            "pred_iou_thresh": args.pred_iou_thresh,
            "stability_score_thresh": args.stability_score_thresh,
            "crop_n_layers": args.crop_n_layers,
            "crop_n_layers_downscale_factor": args.crop_n_layers_downscale_factor,
            "min_area": args.min_area,
        },
        "segmentation_info": {
            "after_sam": sizes[0],
            "after_min_area_filter": sizes[1],
            "after_iou_filter": len(masks),
        },
        "masks": masks_data,
        "annotated_image": str(annotated_path) if args.annotate else "",
    }

    try:
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)
            if len(json_data) == args.size:
                json_data = []  # Truncate result from previous run.
    except FileNotFoundError:
        json_data = []

    json_data.append(json_entry)

    with open(json_path, "w") as json_file:
        json.dump(json_data, json_file, indent=2)
