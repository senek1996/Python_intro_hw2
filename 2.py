# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:57:53 2020

@author: Lenovo
"""

l=[0,1,2,3,4,5,6,7,8,9,10]
ind=0
while ind<len(l)-1:
    l[ind:ind+2]=l[ind:ind+2][::-1]
    ind=ind+2

print('\nПеревернутый список: '+str(l))