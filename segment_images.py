import argparse
import os
from pathlib import Path

import cv2  # type: ignore
import torch
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

from utils.annotate_image import annotate_image
from utils.exclude_small_masks import exclude_small_masks
from utils.intersection_over_union import exclude_masks_by_iou
from utils.save_masks import save_masks

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
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default="D:/GithubProjects/tensorflow_datasets",
)
parser.add_argument("--size", type=int, help="Number of images to segment", default=1)
parser.add_argument(
    "--dataset",
    help="Which dataset to use.",
    default="oxford_flowers102",
    choices=["cifar10", "mnist", "oxford_flowers102", "imagenet2012", "images", "oxford_iiit_pet"],
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
    "-a",
    "--annotate",
    action="store_true",
    help="Enable annotating of image with the computed masks",
)
parser.add_argument(
    "--points_per_side",
    type=int,
    help="The number of points to be sampled along one side of the image. "
    "The total number of points is points_per_side**2.",
    default=32,
)
parser.add_argument(
    "--points_per_batch",
    type=int,
    help="Sets the number of points run simultaneously by the model. Higher numbers may be faster but use more GPU "
    "memory.",
    default=64,
)
parser.add_argument(
    "--pred_iou_thresh",
    type=float,
    help="A filtering threshold in [0,1], using the model's predicted mask quality.",
    default=0.88,
)
parser.add_argument(
    "--stability_score_thresh",
    type=float,
    help="A filtering threshold in [0,1], using the stability of the mask under changes to the cutoff used to "
    "binarize the model's mask predictions.",
    default=0.95,
)
parser.add_argument(
    "--crop_n_layers",
    type=int,
    help="If >0, mask prediction will be run again on crops of the image. Sets the number of layers to run, "
    "where each layer has 2**i_layer number of image crops.",
    default=0,
)
parser.add_argument(
    "--crop_n_layers_downscale_factor",
    type=int,
    help="The number of points-per-side sampled in layer n is scaled down by crop_n_points_downscale_factor**n.",
    default=1,
)
parser.add_argument(
    "--min_area",
    type=float,
    help="Threshold for excluding small masks. 0.01 will remove masks that are smaller than 1% of the image",
    default=0.00,
)
parser.add_argument(
    "--iou_thresh",
    type=float,
    help="Threshold for excluding masks that excede certain IoU with another mask.",
    default=1.0,
)


def register_sam(
    model_type="vit_h",
    checkpoint_path="D:/sam_checkpoints/sam_vit_h_4b8939.pth",
    device="cuda",
    points_per_side=32,
    points_per_batch=64,
    pred_iou_thresh=0.88,
    stability_score_thresh=0.95,
    crop_n_layers=0,
    crop_n_layers_downscale_factor=1,
):
    DEVICE = torch.device(device if torch.cuda.is_available() else "cpu")
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=DEVICE)
    mask_generator = SamAutomaticMaskGenerator(
        sam,
        points_per_side=points_per_side,
        points_per_batch=points_per_batch,
        pred_iou_thresh=pred_iou_thresh,
        stability_score_thresh=stability_score_thresh,
        crop_n_layers=crop_n_layers,
        crop_n_points_downscale_factor=crop_n_layers_downscale_factor,
    )
    return mask_generator, sam, DEVICE


def compute_masks(image, generator: SamAutomaticMaskGenerator):
    """Segments an image into masks using SAM-model"""
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = generator.generate(image_rgb)

    return masks


def get_folder_name(args):
    amg_args = [
        f"pps-{args.points_per_side}",
        f"ppb-{args.points_per_batch}",
        f"pit-{args.pred_iou_thresh}",
        f"sst-{args.stability_score_thresh}",
        f"cnl-{args.crop_n_layers}",
        f"cnldf-{args.crop_n_layers_downscale_factor}",
        f"ma-{args.min_area}",
        f"it-{args.iou_thresh}",
    ]
    folder_name = "_".join(amg_args)
    return f"{args.dataset}_{folder_name}"


def main(args):
    generator, _, _ = register_sam(
        model_type=args.sam_model_type,
        checkpoint_path=args.checkpoint,
        points_per_side=args.points_per_side,
        points_per_batch=args.points_per_batch,
        pred_iou_thresh=args.pred_iou_thresh,
        stability_score_thresh=args.stability_score_thresh,
        crop_n_layers=args.crop_n_layers,
        crop_n_layers_downscale_factor=args.crop_n_layers_downscale_factor,
    )

    img_folder = Path(args.data_path, args.dataset, args.split)

    output_name = get_folder_name(args)
    output_path = Path(args.output, output_name)
    os.makedirs(output_path, exist_ok=True)

    img_folder_files = list(img_folder.iterdir())

    # Loop through the image files and read them
    for i in range(int(args.size)):
        if img_folder_files[i].suffix.lower() not in [".png", ".jpg", ".jpeg"]:
            print("File is not an image, skipping...")
            continue

        img_name, file_type = img_folder_files[i].name.split(".")
        img = cv2.imread(str(img_folder_files[i]))
        print(f"Segmenting {img_name}.{file_type}...")
        masks = compute_masks(img, generator)

        masks_filtered_by_area = exclude_small_masks(masks, args.min_area)
        masks_filtered_by_iou = exclude_masks_by_iou(
            masks_filtered_by_area, args.iou_thresh
        )
        for mask in masks_filtered_by_iou:
            mask["class_id"] = 2
        annotated_path = Path(output_path, f"{img_name}_annotated.png")
        save_masks(
            masks_filtered_by_iou,
            img,
            img_name,
            output_path,
            args,
            [len(masks), len(masks_filtered_by_area)],
            annotated_path,
        )

        if args.annotate:
            annotate_image(masks_filtered_by_iou, img, annotated_path)

    print(f"Done! Result saved in: {str(output_path)}")


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
