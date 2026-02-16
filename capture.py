import cv2
import sys

student_name = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

# Try different camera indexes if 0 fails
for cam_index in [0, 1, 2]:
    cam = cv2.VideoCapture(cam_index)
    ret, frame = cam.read()
    if ret:
        print(f"Camera {cam_index} opened successfully")
        break
    cam.release()
else:
    print("No camera found. Please check your webcam connection.")
    sys.exit()

count = 0
while count < 20:
    ret, frame = cam.read()
    if not ret or frame is None:
        print("Warning: Failed to grab frame from camera.")
        break

    cv2.imshow("Capture Face - Press Q to Save", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(f"../dataset/{student_name}_{count}.jpg", frame)
        print(f"Image {count} saved for {student_name}")
        count += 1

cam.release()
cv2.destroyAllWindows()
