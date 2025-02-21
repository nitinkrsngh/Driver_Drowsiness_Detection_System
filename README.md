# Driver Drowsiness Detection System

Overview

This project implements a real-time driver drowsiness detection system using OpenCV, Python, and deep learning techniques. It monitors the driver's facial landmarks, detects eye aspect ratio (EAR), and classifies drowsiness levels to enhance road safety.

Features

Real-time detection of drowsiness using a webcam.

Eye aspect ratio (EAR) calculation to determine eye closure.

Facial landmark detection for accurate drowsiness assessment.

Alerts the driver when signs of drowsiness are detected.

Technologies Used

Programming Language: Python

Libraries: OpenCV, dlib, imutils, NumPy

Deep Learning: Keras (Optional for advanced detection models)

How It Works

The system captures video frames from the webcam.

It detects facial landmarks and extracts eye coordinates.

The Eye Aspect Ratio (EAR) is calculated to determine if eyes are closed.

If EAR falls below a threshold for a certain period, an alert is triggered.

Usage

Run the script and position your face in front of the webcam.

The system will analyze your eye movements and alert you when drowsiness is detected.

Future Enhancements

Implementing a deep learning model for more accurate detection.

Integrating yawning detection as an additional parameter.

Deploying the system on Raspberry Pi for an in-vehicle solution.

Contributing

Feel free to fork this repository and contribute by improving the detection accuracy or adding new features.

License

This project is licensed under the MIT License.
