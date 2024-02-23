import argparse
from pathlib import Path

import tensorflow_datasets as tfds

parser = argparse.ArgumentParser(description="A script that segments multiple images")
parser.add_argument(
    "--data_path",
    help="Path to the tensorflow_datasets folder",
    default="D:/GithubProjects/tensorflow_datasets",
)
parser.add_argument(
    "--dataset",
    help="Which dataset to use.",
    default="cifar10",
    choices=[
        "cifar10",
        "mnist",
        "oxford_flowers102",
        "imagenet2012",
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
    )


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
