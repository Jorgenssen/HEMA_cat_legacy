#!/usr/bin/python
#-------------------------------------------------------------------------------------
#             FILE: dwarf.py
#      DESCRIPTION: module providing rating tool
#           AUTHOR: Nikita Tatiannikov, n.tatyannikov@gmail.com
#          COMPANY: Tramazzone
#          VERSION: 0.01
# VERSIONS HISTORY: 2018-02-11 (0.01) - base rating logic
#-------------------------------------------------------------------------------------

from fencer import Fencer

def dwarfing(a):
    
    i,j,size = 1,2,len(a)
    while i < size:
        if a[i-1].wins >= a[i].wins:
            i,j = j, j+1
        else:
            a[i-1],a[i] = a[i],a[i-1]
            i -= 1
            if i == 0:
                i,j = j, j+1

    i,j,size = 1,2,len(a)
    while i < size:
        if a[i-1].wins == a[i].wins and (int(a[i-1].hits_got) - int(a[i-1].hits_given)) < (int(a[i].hits_got) - int(a[i].hits_given)):
            a[i-1],a[i] = a[i],a[i-1]
            i,j = j, j+1
        else:
            i -= 1
            if i == 0:
                i,j = j, j+1
    
    return a
