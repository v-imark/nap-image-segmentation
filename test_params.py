import argparse
import json
import os
from pathlib import Path
import random
import subprocess

import cv2
from tqdm import tqdm


PARAMS_PATH = "frontend/static/test_params.json"
OUTPUT_PATH = "frontend/static/data"
DATA_PATH = "D:/GithubProjects/tensorflow_datasets"
DATA_PATH_LAPTOP = "C:/Users/victo/tensorflow_datasets"

parser = argparse.ArgumentParser(description="Tests multiple parameters")

parser.add_argument(
    "--n",
    type=int,
    help="Number of images to test each parameter on",
    default=50,
)
parser.add_argument(
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default=DATA_PATH,
)
parser.add_argument(
    "--param", help="Path to params to use", default="test2", choices=["test1", "test2"]
)


def copy_images(files: list[Path], n, dataset, path):
    random_files = random.sample(files, n)
    image_names = []
    for i in range(int(n)):
        if random_files[i].suffix.lower() not in [".png", ".jpg", ".jpeg"]:
            print("File is not an image, skipping...")
            continue

        img = cv2.imread(str(random_files[i]))
        p = f"{path}/{dataset}/test"
        os.makedirs(p, exist_ok=True)
        cv2.imwrite(f"{p}/{random_files[i].name}", img)
        image_names.append(random_files[i].name)

    with open(f"{path}/{dataset}/image_names.json", "x") as json_file:
        json.dump(image_names, json_file, indent=2)


def get_args(params, args, dataset, path):
    return [
        "python.exe",
        "-m",
        "segment_images",
        "--data_path",
        path,
        "--dataset",
        dataset,
        "--output",
        f"{OUTPUT_PATH}/{args.param}/{params['id']}",
        "--size",
        str(args.n),
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
        "--iou_thresh",
        str(params["iou_thresh"]),
        "-a",
    ]


def main(args):
    with open(PARAMS_PATH, "r") as json_file:
        params_json = json.load(json_file)

    params = params_json[args.param]

    oxford_flowers_files = list(
        Path(args.data_path, "oxford_flowers102", "test").iterdir()
    )
    imagenet_files = list(Path(args.data_path, "imagenet2012", "test").iterdir())
    oxford_pets = list(Path(args.data_path, "oxford_iiit_pet", "test").iterdir())

    IMAGES_OUTPUT_PATH = f"{OUTPUT_PATH}/{args.param}/images"
    os.makedirs(IMAGES_OUTPUT_PATH, exist_ok=True)

    copy_images(oxford_flowers_files, args.n, "oxford_flowers102", IMAGES_OUTPUT_PATH)
    copy_images(imagenet_files, args.n, "imagenet2012", IMAGES_OUTPUT_PATH)
    copy_images(oxford_pets, args.n, "oxford_iiit_pet", IMAGES_OUTPUT_PATH)

    for p in tqdm(params):
        print("Segmenting for:", p["id"])
        im_args = get_args(p, args, "imagenet2012", IMAGES_OUTPUT_PATH)
        of_args = get_args(p, args, "oxford_flowers102", IMAGES_OUTPUT_PATH)
        ofp_args = get_args(p, args, "oxford_iiit_pet", IMAGES_OUTPUT_PATH)

        subprocess.run(im_args)
        subprocess.run(ofp_args)
        subprocess.run(of_args)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
