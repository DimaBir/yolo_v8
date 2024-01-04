import logging
import os
import json
from torchvision import datasets, transforms
import config


def download_coco_dataset():
    """Download and preprocess the COCO dataset."""
    transform = transforms.Compose([
        transforms.Resize(config.IMAGE_SIZE),
        transforms.ToTensor()
    ])

    datasets.CocoDetection(root=config.ROOT_DIR,
                           annFile=config.ANNOTATION_FILE,
                           transform=transform,
                           download=True)
    logging.info("COCO dataset downloaded and preprocessed.")


def convert_coco_annotation_to_yolo():
    """Convert COCO annotations to YOLO format."""
    with open(config.ANNOTATION_FILE) as file:
        coco_annotations = json.load(file)

    for image in coco_annotations['images']:
        image_id = image['id']
        image_filename = os.path.splitext(image['file_name'])[0]
        image_width, image_height = image['width'], image['height']

        annotation_filename = os.path.join(config.YOLO_ANNOTATIONS_DIR, f'{image_filename}.txt')
        with open(annotation_filename, 'w') as yolo_anno_file:
            annotations = [a for a in coco_annotations['annotations'] if a['image_id'] == image_id]
            for annotation in annotations:
                category_id = annotation['category_id']
                bbox = annotation['bbox']
                x_center = (bbox[0] + bbox[2] / 2) / image_width
                y_center = (bbox[1] + bbox[3] / 2) / image_height
                width = bbox[2] / image_width
                height = bbox[3] / image_height

                x_center, y_center, width, height = [round(x, 6) for x in [x_center, y_center, width, height]]
                yolo_anno_file.write(f"{category_id} {x_center} {y_center} {width} {height}\n")


def run_preprocessing():
    logging.basicConfig(level=logging.INFO)
    download_coco_dataset()
    os.makedirs(config.YOLO_ANNOTATIONS_DIR, exist_ok=True)
    convert_coco_annotation_to_yolo()
    logging.info("COCO annotations converted to YOLO format.")


if __name__ == "__main__":
    run_preprocessing()
