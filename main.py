import cv2
import numpy as np
import imutils
import time
import detection as dt
import motors as motors

def updateCamera(cam):
    ret, frame = cam.read()
    frame = imutils.resize(frame, width=600)
    return frame

def updateLineFollow(frame):
    # Check line variation
    pend = [
        dt.line(frame, 400),
        dt.line(frame, 300),
        dt.line(frame, 200),
        dt.line(frame, 100)
    ]

    print(pend)

def updateRescue(frame):
    # Get the circles and show in frame
    circles = dt.circles(frame)
    dt.print(frame, circles)
    
    # Get next command
    ctrl = dt.controller(circles)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'CTRL: ' + str(ctrl),(10,25), font, 0.8,(0,0,0), 1,cv2.LINE_AA)

    # Update the velocity
    vel = dt.getVelocity(ctrl)
    motors.setVelocity(vel)

# Camera
cam = cv2.VideoCapture(0)

cv2.namedWindow('Circle detection')

while True:
    #time.sleep(0.1)

    # Capture the next frame
    frame = updateCamera(cam)

    # LineFollow
    updateLineFollow(frame)

    # Rescue line
    # updateRescue(frame)

    # Show the frame in window
    cv2.imshow('Testing', frame)

    # Exit keys
    key = cv2.waitKey(30) & 0xFF
    if key == 27 or key == ord('q'):
        break

# Release of the program
cam.release()
cv2.destroyAllWindows()