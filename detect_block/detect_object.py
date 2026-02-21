import cv2
from ultralytics import YOLO

model = YOLO("best.pt")
cap = cv2.VideoCapture(0)  # 0 for webcam, or a video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    
    for box in results[0].boxes:
        coords = box.xyxy[0].tolist()
        confidence = box.conf[0].item()
        print(f"Box: {coords}, Confidence: {confidence}")

    cv2.imshow("Result", results[0].plot())  # .plot() draws boxes on the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit
        break

cap.release()
cv2.destroyAllWindows()
