#!/usr/bin/python


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import os

current_path = os.path.dirname(__file__)

def print_time():
    # Use a breakpoint in the code line below to debug your script.
    dt = datetime.datetime.now()
    dt = dt.strftime("%H:%m:%S %d/%m/%y")
    print(f'time = {dt}')  # Press ⌘F8 to toggle the breakpoint.
    with open(f'{current_path}/log.txt', 'a') as file:
        file.write(f'time = {dt}\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_time()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
