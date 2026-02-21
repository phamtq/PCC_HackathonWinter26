from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # start from pretrained weights
model.train(
    data="data.yaml",  # exported from Roboflow
    epochs=50,
    imgsz=640
)
