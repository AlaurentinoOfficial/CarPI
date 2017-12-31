import cv2
import numpy as np

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
    
    if circles is not None:
        circles = np.uint16(np.around(circles)) 
    
    return circles

# Print circles
def printCircles(frame, circles):
    if circles is not None:
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]

            if i[0] > 200 and i[0] < 400:
                cv2.putText(frame, str(center), (i[0] + radius, i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2, 10)

                # circle center
                cv2.circle(frame, center, 1, (0, 100, 100), 3)
                # circle outline
                cv2.circle(frame, center, radius, (0, 255, 255), 3)
            
            else:
                # circle center
                cv2.circle(frame, center, 1, (0, 100, 100), 2)
                # circle outline
                cv2.circle(frame, center, radius, (255, 0, 0), 2)

def controller(circles):
    if circles is not None:
        min = 1000
        dir = 1

        for i in circles[0, :]:
            direction = i[0] - 300
            distance = abs(direction)

            if distance < min:
                min = distance
                dir = direction
        
        buff = 0

        if dir < -100: buff = -1
        elif dir > 100:       buff = 1

        return buff
    else:
        return -1