#!/usr/bin/python3
import time
import datetime
import os
import psutil
from getpass import getpass
from mysql.connector import connect, Error
import datetime
import logging
import sys
from unittest.mock import MagicMock


#current_path = os.path.dirname(__file__)
current_path = os.path.dirname(os.path.realpath(__file__))
#print(f'current path = {current_path}')
path =  current_path + '/log.txt'
#print(path)
if sys.platform != 'linux':
    bluepy_mock = MagicMock()
    p_mock = MagicMock()
    bluepy_mock.btle.Peripheral.return_value = p_mock

    sys.modules['bluepy'] = bluepy_mock
from lywsd02 import Lywsd02Client
def create_client():
    return Lywsd02Client(mac)



mac = 'e7:2e:01:91:69:07'



def print_time():
    try:
        connection = connect(
            host="10.10.10.119",
            user="leon",
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
    #print(f'time = {dt}')  # Press ⌘F8 to toggle the breakpoint.
    #temp = psutil.sensors_temperatures()['scpi_sensors']
    #temp = max(temp[0].current, temp[1].current, temp[2].current, temp[3].current)
    client = create_client()
    #dt = datetime.datetime.now()
    with client.connect():
        temperature = client.temperature
        humidity = client.humidity
        
        with open(path, 'a+') as file:

            file.write(f'time = {dt}: ')
            #for i, sensor in enumerate(temperature):
            file.write(f'{0}-sensor-Balcony -Temp {temperature}-Humidity:{humidity}; ')
            TestRecordInfo = {'Time': dt, 'Sensor': 'Balcony', 'Temperature': temperature}
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
    while True:
        print_time()
        break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
