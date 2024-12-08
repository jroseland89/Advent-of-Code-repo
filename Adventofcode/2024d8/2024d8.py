# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:46:13 2024

@author: Jrose
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 04:57:45 2024

@author: Jrose
"""
import copy
def resonant(input):
    array = (input.splitlines()) #split the input into a list entry per line / report
    finalarray = []
    for eachreport in array: #split each line / report into individual sub-lists with an entry per level
        eachrowsplit = list(eachreport)
        finalarray.append(eachrowsplit)
    #print(finalarray)
    
    #now find all the variables in the array:
    print(len(finalarray))
    
    #first we need to find the gaurd
    antennalist =[]
    for rowid, row in enumerate(finalarray):
        for charid, char in enumerate(row):
            if char == '.':
                continue
            if char not in antennalist:
                antennalist.append(char)
    #print(antennalist)
    
    resonantarray = copy.deepcopy(finalarray)
    
    #now we need to go through each type of antenna in turn
    for antennatype in antennalist:
        #now we need to find each instance of antenna in the array
        for rowid, row in enumerate(finalarray):
            for charid, char in enumerate(row):
                if char == antennatype:
                    antloc = (charid,rowid)
                    antx = charid
                    anty= rowid
                    #print(antloc)
                    #now we need to find the antenna pairs that are resonant with this antenna
                    resonantarray = antipode2(resonantarray, finalarray, antx, anty, antennatype)
    #print(finalarray)
    #print(resonantarray)

    xcount = 0
    
    for row in resonantarray:
        rowcount = row.count('#')
        xcount = xcount + rowcount
    print(xcount)
    
    
def antipode(resonantarray, finalarray, antx, anty, antennatype):
    #check every cell (except the current antenna) for an antenna of the same type
    for rowid, row in enumerate(finalarray):
        for charid, char in enumerate(row):
            #skip curent antenna cell
            if rowid == anty and charid == antx:
                #print('trigger')
                continue
            #find similar antennas
            if finalarray[rowid][charid] == antennatype:
                #print('trigger' + str(charid) + ',' + str(rowid))
                #find the antipode position
                
                antipode1x = charid - (antx - charid)
                antipode1y = rowid - (anty - rowid)
                #print(antipode1x,antipode1y)
                antipode2x = (antx - charid) + antx
                antipode2y = (anty - rowid) + anty
                #check if the antipode position is on the grid
                if  0 <= antipode1x < len(row) and 0 <= antipode1y < len(row):
                    #print('trigger')
                    #append antipode position onto resonantarray
                    resonantarray[antipode1y][antipode1x] = '#'
                if 0 <= antipode2x < len(finalarray) and 0 <= antipode2y < len(finalarray):
                    #append antipode position onto resonantarray
                    resonantarray[antipode2y][antipode2x] = '#'
    return resonantarray
    
def antipode2(resonantarray, finalarray, antx, anty, antennatype):
    #check every cell (except the current antenna) for an antenna of the same type
    for rowid, row in enumerate(finalarray):
        for charid, char in enumerate(row):
            #skip curent antenna cell
            if rowid == anty and charid == antx:
                #print('trigger')
                continue
            #find similar antennas
            if finalarray[rowid][charid] == antennatype:
                #print('trigger' + str(charid) + ',' + str(rowid))
                #find the antipode position
                dif1x = antx - charid
                dif1y = anty - rowid
                dif2x = antx - charid
                dif2y = anty - rowid

                n1 = 1
                while n1 < len(finalarray):
        
                    antipode1x = charid - (dif1x*n1)
                    antipode1y = rowid - (dif1y*(n1))
                    if  0 <= antipode1x < len(row) and 0 <= antipode1y < len(row):
                        #print('trigger')
                        #append antipode position onto resonantarray
                        resonantarray[antipode1y][antipode1x] = '#'
                    
                    antipode2x = (dif2x*n1)+ antx
                    antipode2y = (dif2y*n1) + anty
                    #check if the antipode position is on the grid

                    if 0 <= antipode2x < len(finalarray) and 0 <= antipode2y < len(finalarray):
                        #append antipode position onto resonantarray
                        resonantarray[antipode2y][antipode2x] = '#'
                    n1 += 1
    for rowid, row in enumerate(resonantarray):
        for charid, char in enumerate(row):
            if  resonantarray[rowid][charid] != '.':
                resonantarray[rowid][charid] = '#'
    print(resonantarray)

    return resonantarray
     
            

f = open("input.txt", "r")
input = str(f.read())

resonant(input)