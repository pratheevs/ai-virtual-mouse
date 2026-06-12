Virtual Mouse Using Hand Gesture

A computer vision-based project that enables users to control the mouse cursor using hand gestures captured through a webcam. The system uses hand tracking and gesture recognition to perform mouse operations without requiring a physical mouse.

Technologies Used
Python
OpenCV
MediaPipe
PyAutoGUI
NumPy
Features
Real-time hand tracking
Cursor movement using index finger
Left-click gesture recognition
Webcam-based interaction
Touchless human-computer interaction
Requirements

Install the required libraries:

pip install opencv-python mediapipe pyautogui numpy
How It Works
The webcam captures live video frames.
MediaPipe detects and tracks hand landmarks.
The index finger position is mapped to screen coordinates.
PyAutoGUI moves the mouse cursor based on finger movement.
A click action is performed when the thumb and index finger come close together.
Applications
Touchless computer control
Accessibility assistance
Smart classroom systems
Interactive presentations
Human-computer interaction research
Future Enhancements
Right-click gesture
Double-click gesture
Drag and drop functionality
Volume and brightness control
Screenshot capture gesture
Multi-hand gesture support
Project Outcome

This project demonstrates the integration of Computer Vision and Artificial Intelligence techniques to create a touch-free mouse control system, improving user interaction and accessibility.
