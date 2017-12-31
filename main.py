import cv2
import numpy as np
from detection import detectCircles, printCircles, controller

# Camera
cam = cv2.VideoCapture(0)

while True:
    # Capture the next frame
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)

    # Get the circles and show in frame
    circles = detectCircles(frame)
    printCircles(frame, circles)
    
    # Get next command
    print(controller(circles))

    # Show the frame in window
    cv2.imshow('Circle detection', frame)

    # Exit keys
    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

# Release of the program
cam.release()
cv2.destroyAllWindows()