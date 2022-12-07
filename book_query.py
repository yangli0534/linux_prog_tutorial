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
from pathvalidate import sanitize_filename

lib = BookLibrary(host='10.10.10.250', user='root', database='library', password='oppaha89@A')

# directory = '/volume2/library/books/tmp'
directory = '/volume2/library/books/pilimi-zlib-0-119999'
dest = '/volume2/library/book_lib/'
N = 20
i = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # checking if it is a file
    i = i + 1
    if os.path.isfile(f):

        book = lib.query_with_id(id=int(filename))
        print(f'i={i}: filename = {filename}, book title = {book.title} and author = {book.author},extension={book.extension}')
        new_name = sanitize_filename(f'{book.title}_{book.author}')
        if len(new_name) > 80:
            new_name = new_name[0:79]
        if book.language is None:
            language = 'none'
        else:
            language = book.language
        new_name = f'{new_name}-{filename}.{book.extension}'
        sub_folder = str(int(i/100000))
        dest_new = f'{dest}{language}/{sub_folder}'

        f_dst = os.path.join(dest_new, new_name)
        os.makedirs(dest_new, exist_ok=True)
        os.link(f, f_dst)