import argparse
import json
import os
from pathlib import Path
import subprocess

import cv2
from tqdm import tqdm


PARAMS_PATH = "frontend/static/test_params.json"
OUTPUT_PATH = "frontend/static/data"
IMAGES_OUTPUT_PATH = f"{OUTPUT_PATH}/images"
os.makedirs(IMAGES_OUTPUT_PATH, exist_ok=True)

parser = argparse.ArgumentParser(description="Tests multiple parameters")

parser.add_argument(
    "--n",
    type=int,
    help="Number of images to test each parameter on",
    default=4,
)
parser.add_argument(
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default="D:/GithubProjects/tensorflow_datasets",
)


def copy_images(files: list[Path], n, dataset):
    for i in range(int(n)):
        if files[i].suffix.lower() not in [".png", ".jpg", ".jpeg"]:
            print("File is not an image, skipping...")
            continue

        img = cv2.imread(str(files[i]))
        path = f"{IMAGES_OUTPUT_PATH}/{dataset}/test"
        os.makedirs(path, exist_ok=True)
        cv2.imwrite(f"{path}/{files[i].name}", img)


def get_args(params, n, dataset):
    return [
        "python.exe",
        "-m",
        "segment_images",
        "--data_path",
        IMAGES_OUTPUT_PATH,
        "--dataset",
        dataset,
        "--output",
        f"{OUTPUT_PATH}/{params['id']}",
        "--size",
        str(n),
        "--points_per_side",
        str(params["points_per_side"]),
        "--points_per_batch",
        str(params["points_per_batch"]),
        "--pred_iou_thresh",
        str(params["pred_iou_thresh"]),
        "--stability_score_thresh",
        str(params["stability_score_thresh"]),
        "--crop_n_layers",
        str(params["crop_n_layers"]),
        "--crop_n_layers_downscale_factor",
        str(params["crop_n_layers_downscale_factor"]),
        "--min_area",
        str(params["min_area"]),
        "-a",
    ]


def main(args):
    with open(PARAMS_PATH, "r") as json_file:
        params = json.load(json_file)

    oxford_flowers_files = list(
        Path(args.data_path, "oxford_flowers102", "test").iterdir()
    )
    imagenet_files = list(Path(args.data_path, "imagenet2012", "test").iterdir())

    copy_images(oxford_flowers_files, args.n, "oxford_flowers102")
    copy_images(imagenet_files, args.n, "imagenet2012")

    for p in tqdm(params):
        print("Segmenting for:", p["id"])
        im_args = get_args(p, args.n, "imagenet2012")
        of_args = get_args(p, args.n, "oxford_flowers102")
        subprocess.run(im_args)
        subprocess.run(of_args)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
