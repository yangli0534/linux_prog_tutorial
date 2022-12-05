#!/usr/bin/python

"""
Created on Mon Dec  5 23:22:56 2022

@author: Leon
"""
import time
import datetime
import os
import psutil
from getpass import getpass
from mysql.connector import connect, Error

import Book

class BookLibrary():
    def __init__(self, ip, user, password, port=3306, database='book'):
        try:
            self.connection = connect(
                host=ip,
                user=user,
                password=password,
                database=database,
                auth_plugin="mysql_native_password"
            )
        except Error as e:
            print(e)
            print('failed')

    def query_with_id(self, id):
        query = f""" SELECT * FROM book.books WHERE zlibrary_id = {id};"""

        try:
            with self.connection.cursor() as cursor:
                for result in cursor.execute(query, multi=True):
                    if result.with_rows:
                        tmp = result.fetchall()
                        #print(tmp)

                self.connection.commit()
                # TODO: bug TypeError: 'module' object is not callable
                book = Book(info=tmp[0])
                return book
                # time.sleep(1)
        except Error as e:
            # print('sql operation failed!')
            print(e)

if __name__ == '__main__':
    lib = BookLibrary(ip='10.10.10.119', user='leon', password='oppaha89@A')
    book = lib.query_with_id(id=589518)
    print(book.title)