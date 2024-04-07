import json
import os
from pathlib import Path
import cv2
from flask import Flask, jsonify, request

import sys

import numpy as np

sys.path.append("../")

from backend.annotator import annotator
from backend.filter import filter_and_edit_json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


class NpEncoder(json.JSONEncoder):
    """An encoder that can handle numpy data types."""

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


app.json_provider_class = NpEncoder


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/api/filter", methods=["POST"])
@cross_origin()
def filter_masks():
    query = request.json.get("query")
    os.chdir(os.path.dirname(__file__))
    new_metadata, removed_by_min_area, removed_by_iou, after_iou = filter_and_edit_json(
        query["metadata"], query["min_area"], query["threshold"]
    )
    os.chdir(os.path.dirname(__file__))
    parent_path = Path(Path("./").absolute().parent)
    annotated_path = Path(f"{parent_path}/{new_metadata['annotated_image']}")
    img_path = Path(
        f"{parent_path}/frontend/static/data/test2/images/{new_metadata['dataset']}/test",
        f"{query['img']}",
    )
    img = cv2.imread(str(img_path))
    annotator(img, new_metadata["masks"], annotated_path)

    for mask in new_metadata["masks"]:
        mask.pop("segmentation", None)

    response = jsonify(json.dumps(new_metadata, cls=NpEncoder))

    return response


if __name__ == "__main__":
    app.run(debug=True)
