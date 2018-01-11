#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: fencer.py
#      DESCRIPTION: class module providing the base fencer entity
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.01
# VERSIONS HISTORY: 2018-01-11 (0.01) - base attributes
#-------------------------------------------------------------------------------------

class Fencer():
    def __init__(self, name, club, wins, defeats, hits_got, hist_given):
        self.name = name
        self.club = club
        self.wins = wins
        self.defeats = defeats
        self.hit_got = hit_got
        self.hit_given = hit_given


