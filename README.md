# Object Detection Microservice with YOLO-v8 and COCO Dataset

This project is a microservice-based object detection system using YOLO-v8 for training and the COCO dataset for data. The architecture consists of separate, Dockerized services for data preprocessing, model training, and evaluation. This structure not only facilitates scalability but also makes the system modular and easy to maintain.

## Services

The project is divided into the following services:

1. **Data Preprocessing Service**: Downloads and preprocesses the COCO dataset, making it compatible for use with YOLO-v8.

2. **Model Training Service**: Implements the YOLO-v8 model, training it with the preprocessed COCO dataset.

3. **Model Evaluation Service**: Evaluates the trained model's performance using standard object detection metrics.

Each service is containerized using Docker, ensuring consistent environments and easy deployment.
