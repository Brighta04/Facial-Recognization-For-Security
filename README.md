# Facial-Recognization-For-Security

Face Recognizer with MediaPipe and OpenCV

This project is a real-time face recognition and analysis system built with Python, OpenCV, and MediaPipe. It detects faces via webcam input, analyzes facial orientation, and overlays facial landmarks and information on the video stream.

Features:

Real-time face detection

Facial landmark detection (eyes, lips, mesh)

Face orientation analysis (left, right, straight)

FPS display for performance monitoring

Intuitive mirrored webcam view

Project Structure:

bash Copy Edit face_recognizer/ ├── face_recognizer.py # Main script (provided code) ├── README.md # Project documentation └── requirements.txt # Dependencies file

Requirements:

Python 3.7+

OpenCV

MediaPipe

NumPy

Install dependencies with:

bash Copy Edit pip install -r requirements.txt Example requirements.txt:

Copy Edit opencv-python mediapipe numpy

How to Run Clone the repository or copy the script.

Run the script:

bash Copy Edit python face_recognizer.py The webcam window will open. Press q to exit.

How It Works:

Face Detection: Uses MediaPipe's face detection to find face bounding boxes.

Landmark Detection: Uses MediaPipe's Face Mesh to detect 468 3D face landmarks.

Analysis: Determines whether the face is looking left, right, or straight based on nose position relative to temples.

Display: Draws mesh tesselations, eye and lip contours, orientation text, and FPS.

Notes:

Ensure your webcam is functional and accessible.

For best results, use in a well-lit environment.

You can tweak the min_detection_confidence and max_faces parameters in the constructor for different performance and accuracy levels.

Preview:

Real-time face mesh and orientation analysis.

License: This project is licensed under the MIT License.
