# Gesture-Controlled System

## Overview
This project implements an AI-driven solution for gesture-based control of system settings, focusing on screen brightness and PC volume adjustment. Users can interact with their devices through hand gestures, providing a touch-free and intuitive experience.

## Hand Tracking Module
The hand tracking module utilizes computer vision and machine learning techniques, leveraging OpenCV and MediaPipe. It identifies and tracks hands in real-time, detecting specific landmarks to determine the number of raised fingers.

### Libraries & Tools
- OpenCV (cv2): Comprehensive computer vision library facilitating camera access, image processing, and GUI display.
- MediaPipe: Google's toolbox for interpreting visual data. The "Hands solution" from MediaPipe identifies hands and marks specific landmarks.

## Control of Sound and Screen Brightness
This module enables control over system settings, focusing on speaker volume and screen brightness. Python scripts are used to interact with the system's audio settings (pycaw) and manipulate screen brightness levels (screen_brightness_control).

### Libraries & Tools
- pycaw: Python Core Audio Windows library for interacting with audio settings on Windows OS.
- screen_brightness_control: Python library for manipulating screen brightness levels.

## Main Module
The main module captures video input, identifies hands and the number of raised fingers, and extends functionality to control system settings such as volume and brightness.

### Libraries & Tools Used
- HandTrackingModule1 (hand): An imported module providing functionality for hand detection and landmark identification.
- volumectrl (vol): An imported module enabling control over system settings, particularly volume and brightness.

## Usage
1. Install required dependencies: `pip install -r requirements.txt`
2. Run the main script: `python main.py`
3. Perform hand gestures in front of the camera to control system settings.

Feel free to explore and contribute to enhance gesture recognition capabilities and support additional functionalities.

**Note:** This project is currently designed for Windows OS.
