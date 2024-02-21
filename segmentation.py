import os
import time
from pathlib import Path

import cv2
import torch
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry

sample_image = cv2.imread("./outputs/sample_images/cifar10/test/7.png")


def register_sam(
    points_per_side=32,
    model_type="vit_h",
    checkpoint_path="D:/sam_checkpoints/sam_vit_h_4b8939.pth",
    device="cuda_test",
):
    DEVICE = torch.device(device if torch.cuda.is_available() else "cpu")
    sam = sam_model_registry[model_type](checkpoint=checkpoint_path)
    sam.to(device=DEVICE)
    mask_generator = SamAutomaticMaskGenerator(sam, points_per_side=16)
    mask_generator.generate()
    return mask_generator, sam, DEVICE


def segment_image(image, generator):
    """Segments an image into masks using SAM-model"""
    start_time = time.time()
    print("Segmenting image...")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = generator.generate(image)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Image segmentation complete.", f"Elapsed time: {elapsed_time} seconds.")
    return masks


def save_masks(masks):
    os.makedirs(Path("masks"), exist_ok=True)
    count = 0
    for mask in masks:
        cv2.imwrite(f"masks/mask{count}.png", mask["segmentation"] * 255)
        count += 1
