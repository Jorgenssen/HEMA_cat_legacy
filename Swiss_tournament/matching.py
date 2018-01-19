
#импорт базовых модулей
import csv, sys, locale
import random
from prettytable import PrettyTable
import logging
import logging.config

#импорт внутренних модулей
from fencer import Fencer
from main import index

#выбираем лог-конфиг и логгера
logging.config.fileConfig('log.conf')
logger = logging.getLogger("Inputs") 

random.randint(1, len(index))
print(len(index))

matched_fe = []
matched_op = []
opponent_ID = 0
def matching(index):
    while len(matched_fe)+len(matched_op)+1 < len(index):
        for fencer in index:
            if int(fencer.ID) not in matched_fe:
                opponent_ID = random.randint(1, len(index))
                if opponent_ID not in matched_op and opponent_ID not in matched_fe and opponent_ID != int(fencer.ID) and int(fencer.ID) not in matched_fe and int(fencer.ID) not in matched_op:

                    matched_fe.append(int(fencer.ID))
                    matched_op.append(opponent_ID)



matching(index)
print(matched_fe)
print(matched_op)

table = PrettyTable(['№','Name 1', 'Name 2'])
for i in range(len(matched_fe)):
    table.add_row([i+1,index[matched_fe[i]-1].name, index[matched_op[i]-1].name])
    print(matched_fe[i])
print(table)
