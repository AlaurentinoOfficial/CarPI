
import cv2
import numpy as np
import sys

# -*- coding: UTF-8 -*-

def detectCircles(frame):
    # Create a gray mask
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur
    gray = cv2.medianBlur(gray, 5)
    
    # HoG Circle detection
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=30)   
    
    return circles

# Camera
cam = cv2.VideoCapture(0)

while True:
    # Capture the next frame
    ret, frame = cam.read()

    # Get the circles and show in frame
    circles = detectCircles(frame)
    if circles is not None:
        print(len(circles[0, :]))
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(frame, center, radius, (255, 0, 0), 3)

    # Show the frame in window
    cv2.imshow('Circle detection', frame)

    # Exit keys
    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

# Release of the program
cam.release()
cv2.destroyAllWindows()