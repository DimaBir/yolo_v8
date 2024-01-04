# COCO dataset download and preprocessing configuration
ROOT_DIR = './data'
COCO_YEAR = '2017'
IMAGE_SIZE = (416, 416)
ANNOTATION_FILE = f'{ROOT_DIR}/annotations/instances_train{COCO_YEAR}.json'

# YOLO annotations output configuration
YOLO_ANNOTATIONS_DIR = f'{ROOT_DIR}/yolo_annotations'

# Flask application configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True