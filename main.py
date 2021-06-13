#!/usr/bin/python


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import os
import psutil

current_path = os.path.dirname(__file__)
path = r'//home//leon//code//linux_prog_tutorial//log.txt'
print(path)
def print_time():
    # Use a breakpoint in the code line below to debug your script.
    dt = datetime.datetime.now()
    dt = dt.strftime("%H:%M:%S %d/%m/%y")
    print(f'time = {dt}')  # Press ⌘F8 to toggle the breakpoint.
    temp = psutil.sensors_temperatures()['coretemp']
    #temp = max(temp[0].current, temp[1].current, temp[2].current, temp[3].current)

    with open(path, 'a+') as file:

        file.write(f'time = {dt}: ')
        for i, sensor in enumerate(temp):
            file.write(f'{i}-sensor {sensor.label}-Temp {sensor.current}; ')

        file.write('\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_time()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
