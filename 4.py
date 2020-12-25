# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:10:26 2020

@author: Lenovo
"""

s=input('Введите строку:')
s=s.split(' ')
indx=1
max_len=10 #максимальная длина строки
for ss in s:
    print('\n{0}. {1}'.format(indx,ss[:min(len(ss),max_len)]))    
    indx+=1