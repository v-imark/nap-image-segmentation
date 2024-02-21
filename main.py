import os
from pathlib import Path

import cv2

# load_input_data(dataset="cifar10", size=5)

sample_image = cv2.imread("./outputs/sample_images/cifar10/test/7.png")

image_dir = Path("outputs", "annotated_images", "test")
os.makedirs(image_dir, exist_ok=True)
os.chdir(image_dir)
os.makedirs(Path("masks"), exist_ok=True)
