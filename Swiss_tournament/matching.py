#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: matching.py
#      DESCRIPTION: class module providing the base fencer entity
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.01
# VERSIONS HISTORY: 2018-01-19 (0.01) - base logic of initial (first round) matching
#-------------------------------------------------------------------------------------

#импорт базовых модулей
import random
from prettytable import PrettyTable
import logging
import logging.config

#импорт внутренних модулей
from fencer import Fencer
from main import index

#выбираем лог-конфиг и логгера
logging.config.fileConfig('log.conf')
logger = logging.getLogger("Matching") 

#инициализируем рандомайзер в диапазоне числа наших драчунов
random.randint(1, len(index))

#инициализируем необходимые переменные
matched = []

#магическая функция, которая разбивает наших драчунов на пары
def matching(index):
    not_matched = []
    opponent_ID = 0

    for fencer in index:
        not_matched.append(int(fencer.ID))

    while len(not_matched) > 1:  
        for fencer in not_matched:
            not_matched.remove(fencer)
            opponent_ID = random.choice(not_matched)
            not_matched.remove(opponent_ID)
            matched.append((fencer, opponent_ID))

    if matched:
        matched.append((not_matched[0],'auto_win'))
                            
#проверка списка
print(matched)

#вывод пар
table = PrettyTable(['№','Name 1', 'Name 2'])
for i in range(len(matched)):
    '''
    index[matched_fe[i]-1].name/index[matched_op[i]-1].name - здесь мы обращаемся
    к атрибуту name экземпляра fencer по matched_fe[i]-1,
    где matched_fe[i] - это интовое значение fencer.ID, которое у нас на 1 больше,
    чем порядковый индекс этого же экземпляра в index'e
    '''
    try:
        table.add_row([i+1,index[matched[i][0]-1].name, index[matched[i][1]-1].name])
    except TypeError as err:
        table.add_row([i+1,index[matched[i][0]-1].name, 'auto win'])
   
print(table)
