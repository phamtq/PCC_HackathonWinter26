import cv2, os, glob


# Open the camera
cam = cv2.VideoCapture(0)


# figure out latest capture number
captures = glob.glob("capture_*.jpg")
numbers = []

for i in captures:
  numbers.append(int(i.split('_')[1].split('.')[0]))
numbers.sort()

new_num = 0
if len(numbers) > 0:
  new_num = numbers[-1]+1
print(numbers)
print(new_num)

while True:
  ret, imageFrame = cam.read()

  cv2.imshow('take photos', imageFrame)

  key = cv2.waitKey(1)
  # Press 'q' to exit the loop
  if key == ord('q'):
    break
  elif ret and key == ord('c'):
    cv2.imwrite(f"capture_{new_num}.jpg", imageFrame)
    print(f'{new_num} captured')
    new_num += 1

# Release the capture and writer objects
cam.release()
cv2.destroyAllWindows()


