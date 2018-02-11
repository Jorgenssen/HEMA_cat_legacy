#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: database.py
#      DESCRIPTION: methods for work with database
#           AUTHOR: Arkadiy Kulikov, martin.o.dinnel@gmail.com
#                   Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.02
# VERSIONS HISTORY: 2018-01-16 (0.01) - base raw methodss - create database,
#                                       made a table, ask table and update table
#                                       with new data
#                   2018-01-19 (0.02) - logging was implemented
#-------------------------------------------------------------------------------------

#импорт базовых модулей
import csv, sys, locale, sqlite3
from fencer import Fencer

import logging
import logging.config

#выбираем лог-конфиг и логгера
logging.config.fileConfig('log.conf')
logger = logging.getLogger("Database")


#создаём базу данных
def create_db():
    logger.info('Creating a DB')
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    cursor.executescript("""
        DROP TABLE if exists fencers;
        CREATE TABLE fencers
                    (id integer, name text, club text, wins integer,
                    defeats integer, hits_got integer, hits_given integer, 
                    had_fights_with integer);
    """)
    conn.commit()
    conn.close()
    logger.info('Database created successfully')


#первично пишем драчунов в базу
def first_update(arg):
    logger.info('Initial update to table')
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    for fencer in arg:
        cursor.execute("INSERT INTO fencers VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
        (fencer.ID, fencer.name, fencer.club, fencer.wins, fencer.defeats,
        fencer.hits_got, fencer.hits_given, fencer.had_fights_with))
    conn.commit()
    conn.close()


#дёргаем базу
def ask_table():
    logger.info('Making an update from DB')
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM fencers')
    abc = cursor.fetchall()
    return abc
    conn.close()


#пишем постукавшихся драчунов в базу
def update_table(arg):
    logger.info('Making an update of fights took place')
    conn = sqlite3.connect('fencers.db')
    cursor = conn.cursor()
    for fencer in arg:
        cursor.execute("""UPDATE fencers
                        SET wins = ?, defeats = ?, hits_got = ?, hits_given = ?
                        WHERE id = ?""",
        (fencer.wins, fencer.defeats, fencer.hits_got, fencer.hits_given, fencer.ID))

    conn.commit()
    conn.close()
