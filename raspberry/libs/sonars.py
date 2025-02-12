import time
from threading import Thread
import RPi.GPIO as gpio

#Pins
RIGHT_SONAR_ECHO = 25
RIGHT_SONAR_TRIG = 23
LEFT_SONAR_ECHO = 21
LEFT_SONAR_TRIG = 22

SOUND_SPEED = 340
TRIG_PULSE_DURATION_US = 10

isInitialized = False

def init_sonars():
    if isInitialized:
        return
    
    print("Setting up sonars")
    print(gpio.VERSION)
    print(gpio.RPI_INFO)

    gpio.setmode(gpio.BOARD)
    print("gpio set up to ", gpio.getmode, " mode")

    gpio.setup(RIGHT_SONAR_ECHO, gpio.IN)
    gpio.setup(RIGHT_SONAR_TRIG, gpio.OUT)
    gpio.setup(LEFT_SONAR_ECHO, gpio.IN)
    gpio.setup(LEFT_SONAR_TRIG, gpio.OUT)

    isInitialized = True

# Return right ad left sonar distance
def get_distances():
    if not isInitialized:
        init_sonars()
    
    # Create sound signal
    gpio.output(RIGHT_SONAR_TRIG, gpio.HIGH)
    gpio.output(LEFT_SONAR_TRIG, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(RIGHT_SONAR_TRIG, gpio.LOW)
    gpio.output(LEFT_SONAR_TRIG, gpio.LOW)

    # Wait signal on trig
    #! First el - start time, second el - stop time 
    right_times = [0, 0]
    left_times = [0, 0]

    def get_time(sonar_pin: int, state: int):
        t = 0
        while gpio.input(sonar_pin) == state:
            t = time.time()
        
        if sonar_pin == RIGHT_SONAR_ECHO:
            right_times[state] = t
        else:
            left_times[state] = t
    
    def start_threads(state: int):
        r_sonar_t = Thread(target=get_time, args=(RIGHT_SONAR_ECHO, state))
        l_sonar_t = Thread(target=get_time, args=(LEFT_SONAR_ECHO, state))

        r_sonar_t.start()
        l_sonar_t.start()

        r_sonar_t.join()
        l_sonar_t.join()
        
    start_threads(0)
    start_threads(1)
    
    right_distance = round(((right_times[0] - right_times[1]) * 17150), 2)
    left_distance = round(((left_times[0] - left_times[1]) * 17150), 2)

    return right_distance, left_distance
