import json
import os
from pathlib import Path

import cv2
import numpy as np


def save_masks(masks, image, img_name, output_path, args, initial_size, annotated_path):
    masks_path = Path(output_path, img_name, "masks")
    os.makedirs(masks_path, exist_ok=True)
    json_path = Path(output_path, "metadata.json")
    masks_data = []

    for count, mask in enumerate(masks):
        masked_img = cv2.bitwise_and(
            image, image, mask=mask["segmentation"].astype(np.uint8)
        )
        mask_name = f"{img_name}_mask_{count}.jpeg"
        cv2.imwrite(str(Path(masks_path, mask_name)), masked_img)

        mask_data = {"name": mask_name, "path": str(masks_path), "area": mask["area"]}
        masks_data.append(mask_data)

    json_entry = {
        "name": img_name,
        "dataset": args.dataset,
        "split": args.split,
        "points_per_side": args.points_per_side,
        "min_area": args.min_area,
        "segmentation_info": {
            "initial": initial_size,
            "final": len(masks),
        },
        "masks": masks_data,
        "annotated_image": str(annotated_path) if args.annotate else "",
    }

    try:
        with open(json_path, "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        json_data = []

    json_data.append(json_entry)

    # Step 3: Write the updated data back to the JSON file
    with open(json_path, "w") as json_file:
        json.dump(json_data, json_file, indent=2)
