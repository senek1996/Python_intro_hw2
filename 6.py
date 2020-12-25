# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:45:27 2020

@author: Lenovo
"""

goods=[]
msgs=['название','стоимость','количество','единицу измерения']
meas=['ед','кг','уп']
good={#структура для хранения информации о товаре
      'Название': 'Товар',
      'Цена': 0.0,
      'Количество': 0,
      'Ед_изм': 'ед.'
}
analytics={
    'Название': [],
    'Цена': [],
    'Количество': [],
    'Ед_изм': []
}

#ВВОД ДАННЫХ
ind=1
sub_ind=0
goods_c=good.copy()
inp=input('Товар №'+str(ind)+'. Введите '+msgs[sub_ind]+' товара. При окончании ввода просто нажмите Enter:')
while (inp!=''):
    if sub_ind==0:
        goods_c['Название']=inp
    elif sub_ind==1:
        goods_c['Цена']=float(inp)
    elif sub_ind==2:
        goods_c['Количество']=int(inp)
    else:        
        goods_c['Ед_изм']=meas[int(inp)-1]
        sub_ind=0
        goods.append((ind, goods_c))
        ind=ind+1
        inp=input('Товар №'+str(ind)+'. Введите '+msgs[sub_ind]+' товара. При окончании ввода просто нажмите Enter:')
        goods_c=good.copy()
        continue
        
    
    sub_ind+=1
    if sub_ind<3:        
        inp=input('Товар №'+str(ind)+'. Введите '+msgs[sub_ind]+' товара. При окончании ввода просто нажмите Enter:')
    else:       
        s='\n'
        for i in range(len(meas)):
            s=s+str(i+1)+'. '+meas[i]+' '
        
        #print(s)
        inp=input('Товар №'+str(ind)+'. Введите '+msgs[sub_ind]+' товара (индекс). При окончании ввода просто нажмите Enter. \nПодсказка: '+s)


#СОЗДАНИЕ АНАЛИТИКИ
for elem in goods:
    elem1=elem[1]
    analytics['Название'].append(elem1['Название'])
    analytics['Цена'].append(elem1['Цена'])
    analytics['Количество'].append(elem1['Количество'])
    analytics['Ед_изм'].append(elem1['Ед_изм'])
    

print('\nАналитика товаров:\n')
print(analytics)