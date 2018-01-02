import cv2
import numpy as np

# -*- coding: UTF-8 -*-

def circles(frame):
    # Create a gray mask
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur
    gray = cv2.medianBlur(gray, 5, 5)
    
    # HoG Circle detection
    rows = gray.shape[0]
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 27,
                               param1=100, param2=30,
                               minRadius=1, maxRadius=50)
    
    if circles is not None:
        circles = np.uint16(np.around(circles)) 
    
    return circles

# Print circles
def print(frame, circles):
    if circles is not None:
        for i in circles[0, :]:
            center = (i[0], i[1])
            radius = i[2]

            if i[0] > 200 and i[0] < 400:
                cv2.putText(frame, str(center), (i[0] + radius + 5, i[1] + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2, 10)

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
        return 1

def getVelocity(ctrl):
    if ctrl is 0:
        return (75, 75)
    elif ctrl is 1:
        return (50, -50)
    else:
        return (-50, 50)

lower_black = np.array([30,30,30])
upper_black = np.array([100,100,100])

def line(frame, height, previous=None):
    distance = None

    crop = None
    if previous is None:
        crop = frame[(height-50):(height+50), 0:600]
    else:
        crop = frame[(height-5):(height+5), (previous[0]-25):(previous[0]+25)]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)

    ret,thresh = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
    im2, contours,hierarchy = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        if M['m00'] > 0:
            center = (int(M['m10']/M['m00']), height)

            cv2.circle(frame, center, 3, (0, 0, 255), 3)
            cv2.drawContours(crop, contours, -1, (0,255,0), 1)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,str(center[0] - 300),(center[0] + 10, center[1]), font, 0.8,(255,0,255), 1,cv2.LINE_AA)

            distance = center[0] - 300
    
    return distance