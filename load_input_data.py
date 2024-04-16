import argparse
from pathlib import Path

import tensorflow_datasets as tfds

DATA_PATH = "D:/GithubProjects/tensorflow_datasets"
DATA_PATH_LAPTOP = "C:/Users/victo/tensorflow_datasets"

parser = argparse.ArgumentParser(description="A script that segments multiple images")
parser.add_argument(
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default=DATA_PATH_LAPTOP,
)
parser.add_argument(
    "--dataset",
    help="Which dataset to use.",
    default="oxford_iiit_pet",
    choices=[
        "cifar10",
        "mnist",
        "oxford_flowers102",
        "imagenet2012",
        "oxford_iiit_pet"
    ],
)
parser.add_argument(
    "--split",
    help="Which dataset split to use.",
    default="test",
)


def dir_path(string):
    if Path(string).is_dir():
        return string
    raise NotADirectoryError(string)


def main(args):
    tfds.load(
        args.dataset,
        data_dir=dir_path(args.data_path),
        split=args.split,
        as_supervised=True,
        with_info=True
    )
    


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
