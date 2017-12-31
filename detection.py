
import cv2
import numpy as np
import sys

# Camera
cam = cv2.VideoCapture(0)

while True:
    # Capture the next frame
    ret, frame = cam.read()

    # Show the frame in window
    cv2.imshow('Circle detection', frame)

    # Exit keys
    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

# Release of the program
cam.release()
cv2.destroyAllWindows()