import cv2
import face_recognition
import pickle
import pandas as pd
from datetime import datetime
import os

# Load encodings
data = pickle.loads(open("encodings.pickle", "rb").read())

# Track marked names for this session
marked_names = set()

cam = cv2.VideoCapture(0)

# Daily log file
date = datetime.now().strftime("%Y-%m-%d")
file_path = f"../output/attendance_{date}.csv"
excel_path = file_path.replace(".csv", ".xlsx")

while True:
    ret, frame = cam.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        if True in matches:
            name = data["names"][matches.index(True)]

            if name not in marked_names:
                time = datetime.now().strftime("%H:%M:%S")
                log_entry = pd.DataFrame([[name, date, time]], columns=["Name", "Date", "Time"])

                # Append or create CSV
                if os.path.exists(file_path):
                    log_entry.to_csv(file_path, mode="a", header=False, index=False)
                else:
                    log_entry.to_csv(file_path, index=False)

                # Update Excel (overwrite with combined data)
                if os.path.exists(excel_path):
                    existing = pd.read_excel(excel_path)
                    updated = pd.concat([existing, log_entry], ignore_index=True)
                    updated.to_excel(excel_path, index=False)
                else:
                    log_entry.to_excel(excel_path, index=False)

                marked_names.add(name)
                print(f"{name} marked at {date} {time}")

    cv2.imshow("Attendance System - Press Q to Quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

print("Attendance updated in output folder")