# Remember to include the OpenCV library (pip install opencv-python)
import cv2

# Connect to camera
cam = cv2.VideoCapture(0)

# Capture one frame
ret, frame = cam.read()

if ret:
    cv2.imwrite("captured_image.png", frame)
else:
    print("Failed to capture image.")

cam.release()

image= cv2.imread('captured_image.png')

gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)

contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

number_of_objects_in_image= len(contours)

print ("The number of objects in this image: ", str(number_of_objects_in_image))

