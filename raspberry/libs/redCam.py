import cv2
import numpy as np
import serialPrint as sp

isEnabled = False
video_capture = cv2.VideoCapture(0)

def detect_red_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    return mask

def enable_cam():
    isEnabled = True

def disable_cam():
    isEnabled = False

while isEnabled:
    ret, frame = video_capture.read()
    if not ret:
        break

    red_mask = detect_red_color(frame)

    if cv2.countNonZero(red_mask) > 0:
        print("Красный цвет обнаружен!")
        sp.run_command("05000000000000")
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Red Mask', red_mask)
    cv2.imshow('Red Result', red_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()