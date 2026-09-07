import cv2
import imutils
import datetime

# Load Haar Cascade for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Initialize webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Unable to access the camera.")
    exit()

firstFrame = None
gun_detected_frames = 0  # Counter to avoid false positives

while True:
    ret, frame = camera.read()
    if not ret or frame is None:
        print("Error: Unable to read from camera.")
        break

    # Resize frame for faster processing
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))

    # If guns are detected, draw rectangles and increment counter
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gun_detected_frames += 1

    # Display warning and save frame if gun is consistently detected
    if gun_detected_frames > 5:  # Threshold to confirm gun detection
        print("Gun detected!")
        cv2.putText(frame, "Gun Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # Save the frame where the gun was detected
        cv2.imwrite("gun_detected.jpg", frame)
        break

    # Display timestamp on the frame
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)

    # Show the video feed with detection
    cv2.imshow("Security Feed", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
