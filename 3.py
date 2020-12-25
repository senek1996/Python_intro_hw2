# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 23:18:33 2020

@author: Lenovo
"""

months_list=['Зима','Зима','Весна','Весна','Весна','Лето','Лето','Лето','Осень','Осень','Осень','Зима']
months_dict={
        'Зима': [12,1,2],
        'Весна': [3,4,5],
        'Лето': [6,7,8],
        'Осень': [9,10,11],
    }

num_month=int(input('\nВведите номер месяца от 1 до 12: '))
print('\nЭто {0} (список)'.format(months_list[num_month-1]))
#print('\nЭто {0} (словарь)'.format(months_dict[str(num_month)]))

for x in months_dict: #x - название ключа (строка)
    if num_month in months_dict[x]:
        print('\nЭто {0} (словарь)'.format(x))
        break