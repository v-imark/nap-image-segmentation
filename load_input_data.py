import os
from pathlib import Path

import cv2
import tensorflow_datasets as tfds


def dir_path(string):
    if Path(string).is_dir():
        return string
    raise NotADirectoryError(string)


def load_input_data(
    dataset="imagenet2012",
    data_path="D:/GithubProjects/tensorflow_datasets",
    split="test",
    size=3,
    shuffle=False,
) -> None:
    ds = tfds.load(
        dataset, data_dir=dir_path(data_path), split=split, shuffle_files=shuffle
    )
    samples = ds.take(size)
    data = []

    for sample in samples:
        image, label = sample["image"], sample["label"]
        data.append({"label": label, "image": image.numpy()})

    image_dir = Path("outputs", "sample_images", dataset, split)
    os.makedirs(image_dir, exist_ok=True)
    os.chdir(image_dir)

    for obj in data:
        print(obj["image"])
        cv2.imwrite(f"{obj['label']}.jpeg", obj["image"])
