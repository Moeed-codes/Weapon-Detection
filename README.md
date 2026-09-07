# Gun Detection System

A real-time gun detection system using Python and OpenCV's Haar Cascade classifier. This project utilizes a webcam to detect guns in video frames and automatically captures an image when a detection is confirmed.

## Features
- **Real-time Detection**: Monitors a live video feed from the default webcam.
- **Visual Alerts**: Draws a bounding box around detected guns and displays a "Gun Detected!" warning.
- **Automated Capture**: Saves a snapshot (`gun_detected.jpg`) when a gun is consistently detected (to reduce false positives).
- ** Timestamping**: Displays the current date and time on the video feed.

## Prerequisites
Ensure you have Python installed. You will also need the following libraries:
- `opencv-python`
- `imutils`

## Installation
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install opencv-python imutils
   ```
3. Ensure the `cascade.xml` file is present in the project directory.

## Usage
Run the script using Python:
```bash
python script.py
```

- The webcam feed will open ("Security Feed").
- If a gun is detected, a red warning text will appear, and an image will be saved to the project directory.
- Press **'q'** to quit the application.

## Files
- `script.py`: The main Python script for detection.
- `cascade.xml`: The Haar Cascade trained model for gun detection.
- `gun_detected.jpg`: (Generated) Evidence image of the detected object.
