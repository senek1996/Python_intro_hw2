# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:03:01 2020

@author: Lenovo
"""

rating=[5,4,4,3,2]
x=input('Введите число. Для окончания программы просто нажмите Enter:')
while (x!=''):
    rating.append(int(x))
    rating.sort(reverse=True)
    print('\nРейтинг: {0}'.format(rating))
    x=input('Введите число. Для окончания программы просто нажмите Enter:')