from ultralytics import YOLO
model = YOLO("best.pt")
results = model("captures/capture_193.jpg")
results[0].show()
for box in results[0].boxes:
  coords = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
  confidence = box.conf[0].item()
  print(f"Box: {coords}, Confidence: {confidence}")
