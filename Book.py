#!/usr/bin/python


"""
Created on Mon Dec  5 23:22:56 2022

@author: Leon
"""


class Book():
    def __init__(self, info: tuple):
        # if type(info) != tuple:
        #     raise TypeError
        self.book = info

    @property
    def title(self):
        return self.book[8]

    @property
    def author(self):
        return self.book[9]

if __name__ == '__main__':
    info =  (589518,
 '2019-04-08',
 '2021-04-24',
 'pdf',
 None,
 17433381,
 None,
 'd7ed9d62a269cefabcc43153bc03a783',
 '彩照中国古钱目录',
 '华光普',
 '',
 'chinese',
 '',
 '',
 '',
 '2001',
 '135',
 'Хорошие цветные иллюстрации подлинных литых монет Китая. Полезное дополнение к другим каталогам.',
 'https://covers.zlibcdn2.com/covers/books/d7/ed/9d/d7ed9d62a269cefabcc43153bc03a783.jpg')
    print(type(info))
    print(len(info))
    book = Book(info=info)
    print(book.title)
