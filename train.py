import face_recognition
import pickle
import cv2
import os

dataset_path = "../dataset"
encodings = []
names = []

# Loop through all images in dataset
for filename in os.listdir(dataset_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join(dataset_path, filename)

        # Load image
        image = cv2.imread(filepath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Extract face encodings
        boxes = face_recognition.face_locations(rgb, model="hog")
        encs = face_recognition.face_encodings(rgb, boxes)

        # Parse name from filename
        parts = filename.split("_")
        if len(parts) >= 2:
            # If format is Roll_Name_Index.jpg
            if parts[0].isdigit():
                name = parts[1]   # use the actual name part
            else:
                name = parts[0]   # if no roll number, just take first part
        else:
            name = filename.split(".")[0]  # fallback: whole filename without extension

        # Store encodings
        for enc in encs:
            encodings.append(enc)
            names.append(name)

# Save encodings to file
data = {"encodings": encodings, "names": names}
with open("encodings.pickle", "wb") as f:
    f.write(pickle.dumps(data))

print("Training complete. Encodings saved to encodings.pickle")