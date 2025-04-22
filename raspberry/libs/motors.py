import serialPrint as serp
import sonars as son
import time as tm

def forward(len):
    serp.send_command(f'010{SPEED}00000000')
    tm.sleep(len / SPEED)

def back(len):
    serp.send_command(f'010{-SPEED}00000000')
    tm.sleep(len / SPEED)

def round_right(ROUND_MOVE_TIME):
    serp.send_command(f"0200000{SPEED}0000")
    tm.sleep(ROUND_MOVE_TIME)

def round_left():
    global ROUND_MOVE_TIME
    serp.send_command(f"020{SPEED}00000000")
    tm.sleep(ROUND_MOVE_TIME)

def check_len_to_left_border():
    if son.get_distances()[0] >= 15:
        round_left()
        serp.send_command(f'010{SPEED}00000000')
        round_left()
        forward(STREET_LENGTH_CM)
        round_right()
        serp.send_command(f'010{SPEED}00000000')
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
        serp.send_command(f'010{SPEED}00000000')
        round_right()
        forward(STREET_LENGTH_CM)
        round_left()
        serp.send_command(f'010{SPEED}00000000')
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
            serp.send_command(f'010{SPEED}00000000')
            tm.sleep(ROUND_MOVE_TIME) #TODO: Заменить на расстояние / скорость 
            round_right()
        else:
            round_right()
            serp.send_command(f'010{SPEED}00000000')
            tm.sleep(ROUND_MOVE_TIME) #TODO: Заменить на расстояние / скорость
            round_left()