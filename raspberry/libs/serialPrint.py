import os
import serial as sr

SERIAL_PATH = "/dev/ttyACM0"
isSerialInit = False

def init():
    mod = 666
    os.system(f"sudo chmod {mod} {SERIAL_PATH}")
    os.system(f"stty -F {SERIAL_PATH} -hupcl")

    print(f"init {SERIAL_PATH} to {mod}")
    isSerialInit = True

def showInfo():
    osInfo = os.uname()
    print(f"{osInfo.sysname}, {osInfo.release}, {osInfo.machine}")
    print(f"serial path - {SERIAL_PATH}\n")

#print string command to serial arduino port
def send_command(command: str):
    if not isSerialInit:
        init()

    serial = sr.Serial(SERIAL_PATH)
    serial.write(bytes(command, encoding='utf-8'))
    serial.close()
