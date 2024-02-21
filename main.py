import subprocess
import sys

command = [
    sys.executable,
    "segment_images.py",
    "--sam_model_type",
    "vit_h",
    "--checkpoint",
    "D:/sam_checkpoints/sam_vit_h_4b8939.pth",
    "--points_per_side",
    "8",
    "--data_path",
    "D:/GithubProjects/tensorflow_datasets/cifar10/test",
    "--size",
    "3",
]

subprocess.run(command)
