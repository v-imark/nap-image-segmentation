import cv2
import supervision as sv


def annotate_image(masks, image, path):
    """Annotates an image with the computed masks."""
    mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX)
    detections = sv.Detections.from_sam(masks)
    annotated_image = mask_annotator.annotate(image, detections)
    cv2.imwrite(str(path), annotated_image)
