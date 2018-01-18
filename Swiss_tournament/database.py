#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: database.py
#      DESCRIPTION: methods for work with database
#           AUTHOR: Arkadiy Kulikov, martin.o.dinnel@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.01
# VERSIONS HISTORY: 2018-01-16 (0.01) - base raw methodss - create database,
#                                       made a table, ask table and update table
#                                       with new data
#
#-------------------------------------------------------------------------------------

#импорт базовых модулей
import csv, sys, locale, sqlite3
from fencer import Fencer


#создаём базу данных
def create_db():
    try:
        conn = sqlite3.connect('fencers.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE fencers
                    (id integer, name text, club text, wins integer,
                    defeats integer, hits_got integer, hits_given integer)
                    """)
        pass
    except sqlite3.DatabaseError as err:
        if(err=='Error:  table fencers already exists'):
            print('Everything is ok')
        pass
    conn.close()


#первично пишем драчунов в базу
def first_update(arg):
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    for fencer in arg:
        cursor.execute("INSERT INTO fencers VALUES(?, ?, ?, ?, ?, ?, ?)",
        (fencer.ID, fencer.name, fencer.club, fencer.wins, fencer.defeats,
        fencer.hits_got, fencer.hits_given))
    conn.commit()
    conn.close()


#дёргаем базу
def ask_table():
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fencers')
    abc = cursor.fetchall()
    return abc
    conn.close()


#пишем постукавшихся драчунов в базу
def update_table(arg):
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    for fencer in arg:
        cursor.execute("""UPDATE fencers
                        SET wins = ?, defeats = ?, hits_got = ?, hits_given = ?
                        WHERE id = ?""",
        (fencer.wins, fencer.defeats, fencer.hits_got, fencer.hits_given, fencer.ID))

    conn.commit()
    conn.close()
