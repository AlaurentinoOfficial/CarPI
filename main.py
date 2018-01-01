import cv2
import numpy as np
import time
import detection as dt

def updateCamera(cam):
    ret, frame = cam.read()

    return frame

# Camera
cam = cv2.VideoCapture(0)

while True:
    time.sleep(0.1)

    # Capture the next frame
    frame = updateCamera(cam)

    # Get the circles and show in frame
    circles = dt.circles(frame)
    dt.print(frame, circles)
    
    # Get next command
    ctrl = dt.controller(circles)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'CTRL: ' + str(ctrl),(10,25), font, 0.8,(0,0,0), 1,cv2.LINE_AA)

    # Show the frame in window
    cv2.imshow('Circle detection', frame)

    # Exit keys
    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

# Release of the program
cam.release()
cv2.destroyAllWindows()