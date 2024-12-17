import cv2
import numpy as np
import serial as sr

isSerialInit = False
SERIAL_PATH = '/dev/ttyUSB0'

def init():
    global isSerialInit
    isSerialInit = True
    print("Последовательный порт инициализирован")

def run_command(command: str):
    global isSerialInit
    if not isSerialInit:
        init()

    try:
        serial = sr.Serial(SERIAL_PATH, baudrate=9600, timeout=1)
        serial.write(bytes(command, encoding='utf-8'))
        print(f"Команда '{command}' отправлена через последовательный порт")
        serial.close()
    except Exception as e:
        print(f"Ошибка при отправке команды: {e}")


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

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    red_mask = detect_red_color(frame)

    if cv2.countNonZero(red_mask) > 0:
        print("Красный цвет обнаружен!")
        run_command("RED_DETECTED")
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Red Mask', red_mask)
    cv2.imshow('Red Result', red_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()