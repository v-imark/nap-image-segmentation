import asyncio
import json
import os
from pathlib import Path
import cv2
from flask import Flask, jsonify, request

import sys

import numpy as np


sys.path.append("../")

from backend.transparent_background import make_bg_transparent
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


def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped


def perform_task(metadata, min_area, threshold, img):
    os.chdir(os.path.dirname(__file__))
    new_metadata, _, _, _ = filter_and_edit_json(metadata, min_area, threshold)
    os.chdir(os.path.dirname(__file__))
    parent_path = Path(Path("./").absolute().parent)
    annotated_path = Path(f"{parent_path}/{new_metadata['annotated_image']}")
    img_path = Path(
        f"{parent_path}/frontend/static/data/test2/images/{new_metadata['dataset']}/test",
        f"{img}",
    )
    img = cv2.imread(str(img_path))
    annotator(img, new_metadata["masks"], annotated_path)

    for mask in new_metadata["masks"]:
        mask.pop("segmentation", None)

    return new_metadata


@background
def parallel_task(metadata, min_area, threshold, img):
    return perform_task(metadata, min_area, threshold, img)


@app.route("/api/filter", methods=["POST"])
@cross_origin()
def filter_masks():
    query = request.json.get("query")

    new_metadata = perform_task(
        query["metadata"], query["min_area"], query["threshold"], query["img"]
    )

    response = jsonify(json.dumps(new_metadata, cls=NpEncoder))

    return response


@app.route("/api/filter_all", methods=["POST"])
@cross_origin()
def filter_all_masks():
    query = request.json.get("query")

    metadatas = query["metadata"]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    looper = asyncio.gather(
        *[
            parallel_task(
                img_metadata,
                query["min_area"],
                query["threshold"],
                f"{img_metadata['name']}.{query['suffix']}",
            )
            for img_metadata in metadatas
        ]
    )

    results = loop.run_until_complete(looper)

    response = jsonify(json.dumps(results, cls=NpEncoder))
    return response


@app.route("/api/transparent", methods=["POST"])
@cross_origin()
def transparent_masks():
    query = request.json.get("query")
    os.chdir(os.path.dirname(__file__))

    for mask in query["masks"]:
        path = Path(Path("./").absolute().parent, mask["path"])
        make_bg_transparent(f"{Path(path, mask['name'])}")

    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run(debug=True)
