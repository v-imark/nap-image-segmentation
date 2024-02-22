import argparse
import csv
import os
from pathlib import Path

import cv2  # type: ignore
import numpy as np
import torch
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

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
    help="Path to the folder containing the images",
    default="D:/GithubProjects/tensorflow_datasets/cifar10/test",
)
parser.add_argument("--size", type=int, help="Number of images to segment", default=3)


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
    # start_time = time.time()
    print("Segmenting image...")
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = generator.generate(image_rgb)
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("Image segmentation complete.", f"Elapsed time: {elapsed_time} seconds.")

    # Todo: exclude small masks

    # Todo: exclude overlapping masks using IoU

    return masks


def save_masks(masks, image, img_name, output_path):
    masks_path = Path(output_path, img_name, "masks")
    os.makedirs(masks_path, exist_ok=True)

    csv_data = []
    for count, mask in enumerate(masks):
        masked_img = cv2.bitwise_and(
            image, image, mask=mask["segmentation"].astype(np.uint8)
        )
        mask_name = f"{img_name}_mask_{count}.mask"
        cv2.imwrite(str(Path(masks_path, f"{mask_name}.jpeg")), masked_img)
        csv_data.append([str(masks_path), mask_name, "jpeg", mask["area"]])

    with open(Path(output_path, "metadata.csv"), "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)


def main(args):
    generator, _, _ = register_sam(
        model_type=args.sam_model_type,
        checkpoint_path=args.checkpoint,
        points_per_side=args.points_per_side,
    )

    img_folder = Path(args.data_path)

    # Will change these later
    output_name = f"cifar10_{args.size}"
    output_path = Path("outputs", output_name)
    os.makedirs(output_path, exist_ok=True)

    img_folder_files = list(img_folder.iterdir())

    # Loop through the image files and read them
    for i in range(int(args.size)):
        if str(img_folder_files[i]).lower().endswith((".png", ".jpg", ".jpeg")):
            img_name, _ = img_folder_files[i].name.split(".")
            img = cv2.imread(str(img_folder_files[i]))

            masks = compute_masks(img, generator)
            save_masks(masks, img, img_name, output_path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
