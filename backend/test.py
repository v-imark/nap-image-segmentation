import json
import os
from pathlib import Path
import sys

import cv2
from matplotlib import pyplot as plt
import supervision as sv

sys.path.append("../")
from backend.annotator import annotator
from backend.filter import filter_and_edit_json

path = Path(
    "D:/GithubProjects/nap-image-segmentation/frontend/static/data/test2/default/oxford_flowers102_pps-32_ppb-64_pit-0.88_sst-0.95_cnl-0_cnldf-1_ma-0.0_it-1.0/metadata.json"
)

with open(path, "r") as json_file:
    data = json.load(json_file)

metadata = data[2]
min_area = 0.01
threshold = 0.6

new_metadata, removed_by_min_area, removed_by_iou, after_iou = filter_and_edit_json(
    metadata, min_area, threshold
)
os.chdir(os.path.dirname(__file__))
parent_path = Path(Path("./").absolute().parent)
annotated_path = Path(f"{parent_path}/{new_metadata['annotated_image']}")
img_path = Path(
    f"{parent_path}/frontend/static/data/test2/images/{new_metadata['dataset']}/test",
    f"{new_metadata['name']}.jpg",
)
img = cv2.imread(str(img_path))
anno = annotator(img, new_metadata["masks"], annotated_path)
sv.plot_image(anno)
sv.plot_image(img)
