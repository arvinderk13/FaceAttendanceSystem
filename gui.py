import tkinter as tk
import subprocess

# Function to run capture.py with student name
def run_capture():
    student_name = entry_name.get().strip()
    if student_name == "":
        print("Please enter a student name")
        return
    subprocess.run(["python", "capture.py", student_name])

# Function to run train.py
def run_train():
    subprocess.run(["python", "train.py"])

# Function to run attendance.py
def run_attendance():
    subprocess.run(["python", "attendance.py"])

# Create main window
root = tk.Tk()
root.title("Face Attendance System")
root.geometry("400x350")

# Heading
heading = tk.Label(root, text="Face Attendance System", font=("Arial", 16, "bold"))
heading.pack(pady=20)

# Input field for student name
label_name = tk.Label(root, text="Enter Student Name:")
label_name.pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

# Buttons
btn_capture = tk.Button(root, text="Capture Student Images", command=run_capture, width=25, height=2)
btn_capture.pack(pady=10)

btn_train = tk.Button(root, text="Train Model", command=run_train, width=25, height=2)
btn_train.pack(pady=10)

btn_attendance = tk.Button(root, text="Start Attendance", command=run_attendance, width=25, height=2)
btn_attendance.pack(pady=10)

# Run GUI loop
root.mainloop()