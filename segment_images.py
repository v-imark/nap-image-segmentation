import argparse
import csv
import os
from pathlib import Path

import cv2  # type: ignore
import numpy as np
import torch
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

from utils.exclude_small_masks import exclude_small_masks
from utils.save_filter_data import save_filter_data

parser = argparse.ArgumentParser(description="A script that segments multiple images")
parser.add_argument(
    "--sam_model_type",
    help="Segment-Anything model type.",
    choices=["vit_h", "vit_l", "vit_b"],
    default="vit_h",
)
parser.add_argument(
    "--checkpoint",
    help="Path to SAM checkpoint.",
    default="D:/sam_checkpoints/sam_vit_h_4b8939.pth",
)
parser.add_argument(
    "--points_per_side",
    type=int,
    help="The number of points to be sampled along one side of the image. "
    "The total number of points is points_per_side**2.",
    default=32,
)
parser.add_argument(
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default="D:/GithubProjects/tensorflow_datasets",
)
parser.add_argument("--size", type=int, help="Number of images to segment", default=3)
parser.add_argument(
    "--dataset",
    help="Which dataset to use.",
    default="cifar10",
    choices=["cifar10", "mnist", "oxford_flowers102", "imagenet2012"],
)
parser.add_argument(
    "--split",
    help="Which dataset split to use.",
    default="test",
)
parser.add_argument(
    "--output",
    help="Path to where the output will be stored",
    default="./outputs",
)
parser.add_argument(
    "--min_area",
    type=float,
    help="Threshold for excluding small masks. 0.01 will remove masks that are smaller than 1% of the image",
    default=0.01,
)


def register_sam(
    model_type="vit_h",
    checkpoint_path="D:/sam_checkpoints/sam_vit_h_4b8939.pth",
    device="cuda",
    points_per_side=32,
):
    DEVICE = torch.device(device if torch.cuda.is_available() else "cpu")
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=DEVICE)
    mask_generator = SamAutomaticMaskGenerator(sam, points_per_side=points_per_side)
    return mask_generator, sam, DEVICE


def compute_masks(image, generator: SamAutomaticMaskGenerator):
    """Segments an image into masks using SAM-model"""
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = generator.generate(image_rgb)

    return masks


def save_masks(masks, image, img_name, output_path):
    masks_path = Path(output_path, img_name, "masks")
    os.makedirs(masks_path, exist_ok=True)
    csv_path = Path(output_path, "metadata.csv")

    csv_data = []
    if not os.path.exists(csv_path):
        csv_data.append(["path", "name", "area"])

    for count, mask in enumerate(masks):
        masked_img = cv2.bitwise_and(
            image, image, mask=mask["segmentation"].astype(np.uint8)
        )
        mask_name = f"{img_name}_mask_{count}.jpeg"
        cv2.imwrite(str(Path(masks_path, mask_name)), masked_img)
        csv_data.append([str(masks_path), mask_name, mask["area"]])

    with open(csv_path, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)


def main(args):
    generator, _, _ = register_sam(
        model_type=args.sam_model_type,
        checkpoint_path=args.checkpoint,
        points_per_side=args.points_per_side,
    )

    img_folder = Path(args.data_path, args.dataset, args.split)

    output_name = (
        f"{args.dataset}_{args.split}_{args.size}_{args.points_per_side}_{args.thresh}"
    )
    output_path = Path(args.output, output_name)
    os.makedirs(output_path, exist_ok=True)

    img_folder_files = list(img_folder.iterdir())

    # Loop through the image files and read them
    for i in range(int(args.size)):
        if img_folder_files[i].suffix not in [".png", ".jpg", ".jpeg"]:
            print("File is not an image, skipping...")
            continue

        img_name, file_type = img_folder_files[i].name.split(".")
        img = cv2.imread(str(img_folder_files[i]))
        print(f"Segmenting {img_name}.{file_type}...")
        masks = compute_masks(img, generator)
        masks_filtered = exclude_small_masks(masks, args.thresh)
        save_masks(masks_filtered, img, img_name, output_path)
        save_filter_data(masks, masks_filtered, args.thresh, output_path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
