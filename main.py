#!/usr/bin/python


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import os
import psutil
from getpass import getpass
from mysql.connector import connect, Error

current_path = os.path.dirname(os.path.realpath(__file__))
#print(f'current path = {current_path}')
path =  current_path + '/log.txt'

def print_time():
    try:
        connection = connect(
            host="10.10.10.101",
            user="root",
            password="oppaha89@A",
            database="sql_temperature",
            auth_plugin="mysql_native_password"
        )
    except Error as e:
        print(e)
        print('failed')

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
            TestRecordInfo = {'Time': dt, 'Sensor': sensor.label, 'Temperature': sensor.current}
            update_query = """
                    INSERT INTO
                    `temp_tbl`(
                        `Time`,
                        `Sensor`,
                        `Temperature`

                    )
                    VALUES(
                            '%s', '%s', %f
                        );
                    """ % (
                # Sn, RunMode, StartTime, MpgName, MpgTestTime, AppRev, MpName, MpTestTime, LimitDown, LimitUp, Result
                TestRecordInfo['Time'], TestRecordInfo['Sensor'], TestRecordInfo['Temperature']
            )
            try:
                with connection.cursor() as cursor:
                    for result in cursor.execute(update_query, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                    connection.commit()
                    # time.sleep(1)
            except Error as e:
                # print('sql operation failed!')
                print(e)

        file.write('\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_time()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
