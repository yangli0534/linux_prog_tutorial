# -*- coding: utf-8 -*-

#!/usr/bin/python
"""
Created on Mon Dec  5 23:08:56 2022

@author: Leon
"""

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import os,sys
#import psutil
from BookLibrary import BookLibrary
from slugify import slugify

lib = BookLibrary(host='10.10.10.250', user='root', database='library', password='oppaha89@A')

directory = '/volume2/library/books/pilimi-zlib-120000-419999/'
dest = '/volume2/library/book_lib'
N = 20
i = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file
    i = i + 1
    if os.path.isfile(f) and i < N:

        book = lib.query_with_id(id=int(filename))
        print(f'filename = {filename}, book title = {book.title} and author = {book.author}')
        new_name = slugify(f'{book.title}_{book.author}', max_length=80, word_boundary=False, separator=' ',)

        new_name = f'{new_name}-{filename}.{book.extension}'
        f_dst = os.path.join(dest, new_name)
        os.link(f, f_dst)