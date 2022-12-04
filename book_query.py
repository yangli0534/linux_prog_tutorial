#!/usr/bin/python


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import os
import psutil
from getpass import getpass
from mysql.connector import connect, Error

try:
    connection = connect(
        host="10.10.10.119",
        user="leon",
        password="oppaha89@A",
        database="book",
        auth_plugin="mysql_native_password"
    )
except Error as e:
    print(e)
    print('failed')

query = """ SELECT * FROM book.books WHERE language = 'Chinese';"""

try:
    with connection.cursor() as cursor:
        for result in cursor.execute(query, multi=True):
            if result.with_rows:
                print(result.fetchall())
        connection.commit()
        # time.sleep(1)
except Error as e:
    # print('sql operation failed!')
    print(e)