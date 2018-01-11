#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: try_doubles.py
#      DESCRIPTION: counting of doublehits and stopping fight
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.02
# VERSIONS HISTORY: 2017-12-08 (0.01) - base logic
#                   2017-12-08 (0.02) - fixed bug "infinity after 2"
#-------------------------------------------------------------------------------------

'''
Это функция-имитатор ситуации после начисления очков.
Предполагаемый триггер ее срабатывания - нажатие кнопки "обоюдка" в операторской гуе.
'''

def dubles():
    k = 0 # вспомогательный счетчик 
    d = 0 # счетчик собственно обоюдок
    
    while d <= 4:
        if input('doublehit '): # имитируем нажатие кнопки "обоюдка"
            d += 1 
            k += 1
        else:
            if k == 2 or k ==1: 
                k -= 1
                '''
                Здесь делаем магию.
                При отсутствии обоюдки нам надо имитировать понятие "не подряд". Имитируем мы его уменьшением дополнительного счетчика.
                Проверка значений дополнительного счетчика нужна для того, чтобы он изменялся только в том случае, если у нас уже были обоюдки.
                '''
        if d == 4: # 4 обоюдки за бой - идем домой
            print('Ой всё, оба домой')
            break
        elif d != 4 and k == 3: # 3 подряд - тоже идем домой
            print('Господа, так нельзя!')
            break
                
dubles()
