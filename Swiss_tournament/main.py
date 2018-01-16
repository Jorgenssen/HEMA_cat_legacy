#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: fencer.py
#      DESCRIPTION: class module providing the base fencer entity
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.00
# VERSIONS HISTORY: 2018-01-14 (0.01) - there were added import of class Fencer and
#                                       func indexing() from inputs, and input flow
#                                       now is defined here
#-------------------------------------------------------------------------------------


from fencer import Fencer
from inputs import indexing, making_update
from database import create_db, first_update, ask_table, update_table
from prettytable import PrettyTable

#Вводим стартовый протокол
index = []
input_file = "test-list.csv"
indexing(input_file, index)

update = []
test_update = "test-update.csv"
making_update(test_update, update)
'''
    После выполнения функции indexing(*args) мы получили список index, где содержатся
сгенерированные экземпляры класса Fencer (наши дорогие драчуны).
    Все манипуляции по матчингу, построению рейтинга и т.д. должны выполняться либо
непосредственно с этим списком, либо с его копиями.
'''

#Проверяем стартовый протокол
# table = PrettyTable(['ID', 'name', 'club', 'wins', 'defeats', 'hits_got', 'hits_given'])
# for fencer in index:
#    table.add_row([fencer.ID,fencer.name,fencer.club,fencer.wins,fencer.defeats,fencer.hits_got,fencer.hits_given])
# print(table)

#создаём базу
create_db()

#вбрасываем первых ребят
first_update(index)

#прописываем подравшихся драчунов
update_table(update)

#дёргаем текущую версию базы
for x in ask_table():
     print(x)
