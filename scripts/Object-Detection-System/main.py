# Import
import cv2
import numpy as np
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Load YOLO model and weights
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load COCO names file to recognize classes
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Get the output layer names in the architecture
layer_names = net.getLayerNames()

# Fix for different OpenCV versions
try:
    # Older OpenCV versions (where getUnconnectedOutLayers returns a 2D array)
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
except IndexError:
    # Newer OpenCV versions (where getUnconnectedOutLayers returns a 1D array)
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Main Class
class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection System")
        self.root.geometry("800x600")  # Using 800x600 resolution due to hardware limitations. Feel free to change it though.
        
        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.start_button = tk.Button(root, text="Start Detection", command=self.start_detection)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Detection", command=self.stop_detection, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.cap = None
        self.is_running = False

    def start_detection(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.cap = cv2.VideoCapture(0)
        self.is_running = True

        self.detect_objects()

    def stop_detection(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.is_running = False
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()

    def detect_objects(self):
        # Load the YOLO model
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]

        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                break

            height, width, _ = frame.shape
            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            if len(indexes) > 0:
                for i in indexes.flatten():
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    color = (0, 255, 0)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            # Convert the frame to a format Tkinter can display (RGB)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the video label with the new frame
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

            # Schedule the next frame update
            self.root.update()

# Create the main window
root = tk.Tk()
app = ObjectDetectionApp(root)
root.mainloop()