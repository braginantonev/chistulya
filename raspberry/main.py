import libs.serialPrint as serp
import libs.redCam as cam
import libs.sonars as son
import time as tm

SPEED = 100

#! Расстояние временное, должно получаться с сервера
STREET_LENGTH_CM = 1000

son.init_sonars()
serp.showInfo()

def forward(len):
    serp.run_command(f'010{SPEED}00000000')
    tm.sleep(len / SPEED)


def round_right():
    global ROUND_MOVE_TIME
    serp.run_command(f"0200000{SPEED}0000")
    tm.sleep(ROUND_MOVE_TIME)


def round_left():
    serp.run_command(f"020{SPEED}00000000")
    tm.sleep(ROUND_MOVE_TIME)


def check_len_to_left_border():
    if son.get_distances()[0] >= 15:
        round_left()
        serp.run_command(f'010{SPEED}00000000')
        round_left()
        forward(STREET_LENGTH_CM)
        round_right()
        serp.run_command(f'010{SPEED}00000000')
        round_right()
        return True
    else:
        round_left()
        round_left()
        forward(STREET_LENGTH_CM)
        round_left()
        round_left()
        return False
    
def check_len_to_right_border():
    if son.get_distances()[1] >= 15:
        round_right()
        serp.run_command(f'010{SPEED}00000000')
        round_right()
        forward(STREET_LENGTH_CM)
        round_left()
        serp.run_command(f'010{SPEED}00000000')
        round_left()
        return True
    else:
        round_left()
        round_left()
        forward(STREET_LENGTH_CM)
        round_left()
        round_left()
        return False


def find_center():
    distances = son.get_distances()
    if distances[0] != distances[1]:
        move_len = abs(distances[0] - distances[1]) / 2
        ROUND_MOVE_TIME = move_len / SPEED
        if distances[0] < distances[1]:
            round_left()
            serp.run_command(f'010{SPEED}00000000')
            tm.sleep(ROUND_MOVE_TIME) #TODO: Заменить на расстояние / скорость 
            round_right()
        else:
            round_right()
            serp.run_command(f'010{SPEED}00000000')
            tm.sleep(ROUND_MOVE_TIME) #TODO: Заменить на расстояние / скорость
            round_left()


while True:
    find_center()
    
    while check_len_to_left_border:
        forward(STREET_LENGTH_CM)
        
        check_len_to_left_border()

    while check_len_to_right_border:
        forward(STREET_LENGTH_CM)
        
        check_len_to_left_border()
    break





