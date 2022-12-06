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

from Book import Book

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
        query_isbn = f""" SELECT * FROM book.isbn WHERE zlibrary_id = {id};"""
        try:
            with self.connection.cursor() as cursor:
                for result in cursor.execute(query, multi=True):
                    if result.with_rows:
                        tmp = result.fetchall()
                        #print(tmp)

                self.connection.commit()
                # TODO: bug TypeError: 'module' object is not callable

                # time.sleep(1)
        except Error as e:
            # print('sql operation failed!')
            print(e)

        try:
            with self.connection.cursor() as cursor:
                for result in cursor.execute(query_isbn, multi=True):
                    if result.with_rows:
                        tmp1 = result.fetchall()
                        # print(tmp)

                self.connection.commit()
                # TODO: bug TypeError: 'module' object is not callable

                # time.sleep(1)
        except Error as e:
            # print('sql operation failed!')
            print(e)
        if len(tmp) > 0 and len(tmp1) > 0:
            book = Book(info=tmp[0], isbn=tmp1[0])
            return book
        elif len(tmp) == 0:
            book = Book(info=None, isbn=None)
            return book
        elif len(tmp1) == 0:
            book = Book(info=tmp[0], isbn=None)
            return book

if __name__ == '__main__':
    lib = BookLibrary(ip='172.16.1.35', user='root', password='leonfromzillnk')
    #book = lib.query_with_id(id=18419)
    for i in range(177, 200):
        book = lib.query_with_id(id=i)
        # print(book.title)
        # print(book.author)
        # print(book.isbn)
        print(f'zlibrary id = {i}, book name = {book.title}, book author = {book.author}, isbn = {book.isbn}')
