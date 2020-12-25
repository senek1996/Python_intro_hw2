# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:52:27 2020

@author: Lenovo
"""

l=[]

#заполнение списка
l.append(23)
l.append(23.0)
l.append(True)
l.append('qwerty')

for elem in l:
    print(str(type(elem))+'\n')