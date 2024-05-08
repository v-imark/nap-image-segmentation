import cv2
import numpy as np
import supervision as sv


def annotate_image(masks, image, path, color=sv.ColorPalette.DEFAULT, opacity=0.5):
    """Annotates an image with the computed masks."""
    mask_annotator = sv.MaskAnnotator(
        color=color, opacity=opacity, color_lookup=sv.ColorLookup.CLASS
    )
    polygon_annotator = sv.PolygonAnnotator(
        color=color, thickness=2, color_lookup=sv.ColorLookup.CLASS
    )

    # sorted_generated_masks = sorted(masks, key=lambda x: x["area"], reverse=True)
    sorted_generated_masks = masks
    xywh = np.array([mask["bbox"] for mask in sorted_generated_masks])
    mask_imgs = np.array([mask["segmentation"] for mask in sorted_generated_masks])
    class_id = np.array([mask["class_id"] for mask in sorted_generated_masks])
    xyxy = xywh.copy()
    xyxy[:, 2] = xywh[:, 0] + xywh[:, 2]
    xyxy[:, 3] = xywh[:, 1] + xywh[:, 3]
    detections = sv.Detections(xyxy=xyxy, mask=mask_imgs, class_id=class_id)

    annotated_image = mask_annotator.annotate(image, detections)
    annotated_image = polygon_annotator.annotate(annotated_image, detections)
    cv2.imwrite(str(path), annotated_image)
    return annotated_image
