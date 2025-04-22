import libs.serialPrint as serp
#import libs.redCam as cam
#import libs.sonars as son
import libs.server as server
import time as tm
import threading

SPEED = 100

#TODO: Доделать алгоритм уборки
def start_cleaning(street_length: float): 
    pass

#TODO: Добавить описание 15 команды в доки
def run_command(command: str):
    if command[:2] == "15":
        start_cleaning(0) #TODO: Заменить на значение из первого параметра
    else:
        serp.send_command(command)

server_thread = threading.Thread(target=server.run)
server_thread.start()

serp.showInfo()

while (True):
    command = server.get_command() # Command, time
    if command == None:
        tm.sleep(1)
        continue
    
    print(f"run_command {command[0]} in time {command[1]}")
    run_command(command[0])
    tm.sleep(command[1])
    server.complete_command()
    tm.sleep(0.5) # Delay