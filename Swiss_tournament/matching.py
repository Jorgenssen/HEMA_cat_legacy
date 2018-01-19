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
matched_fe = []
matched_op = []
opponent_ID = 0

#магическая функция, которая разбивает наших драчунов на пары
def matching(index):
    while len(matched_fe)+len(matched_op)+1 < len(index):
        for fencer in index:
            if int(fencer.ID) not in matched_fe and int(fencer.ID) not in matched_op:
                opponent_ID = random.randint(1, len(index))
                if opponent_ID not in matched_op and opponent_ID not in matched_fe and opponent_ID != int(fencer.ID):

                    matched_fe.append(int(fencer.ID))
                    matched_op.append(opponent_ID)

#вызов функции должен быть перенесен в main.py
matching(index)

#проверка списков
print(matched_fe)
print(matched_op)

#вывод пар
table = PrettyTable(['№','Name 1', 'Name 2'])
for i in range(len(matched_fe)):
    '''
    index[matched_fe[i]-1].name/index[matched_op[i]-1].name - здесь мы обращаемся
    к атрибуту name экземпляра fencer по matched_fe[i]-1,
    где matched_fe[i] - это интовое значение fencer.ID, которое у нас на 1 больше,
    чем порядковый индекс этого же экземпляра в index'e
    '''
    table.add_row([i+1,index[matched_fe[i]-1].name, index[matched_op[i]-1].name])
#добавляем в таблицу бойца с автопобедой
for fencer in index:
    if int(fencer.ID) not in matched_fe and int(fencer.ID) not in matched_op:
        '''
        len(matched_fe)+1 - выводим порядковый номер на 1 больше, чем было боев уже
        (длина списка matched_fe/matched_op равна количеству боев)

        index[int(fencer.ID)-1].name - обращаемся к атрибуту name эземпляра fencer,
        где fencer.ID на 1 больше, чем порядковый индекс экземпляра в index
        '''
        table.add_row([len(matched_fe)+1, index[int(fencer.ID)-1].name, 'auto-win'])
    
print(table)
