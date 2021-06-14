# -*- coding: utf-8 -*-
"""
Created by Leon at 6/15/2021
"""
__author__ = "Leon"
__version__ = "0.0.1"
__email__ = "yangli0534@gmail.com"

import time
import datetime
import os
from getpass import getpass
from mysql.connector import connect, Error

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

time.sleep(1)

dt = datetime.datetime.now()
dt = dt.strftime("%H:%M:%S %d/%m/%y")
TestRecordInfo = {'Time': dt, 'Sensor': 'core 1', 'Temperature': 55}
#mysql_operate(TestRecordInfo)

#
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
print(update_query)
    # time.sleep(0.5)

c
    #return
