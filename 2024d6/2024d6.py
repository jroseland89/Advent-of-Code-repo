# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 04:57:45 2024

@author: Jrose
"""

def gaurds(input):
    array = (input.splitlines()) #split the input into a list entry per line / report
    finalarray = []
    for eachreport in array: #split each line / report into individual sub-lists with an entry per level
        eachrowsplit = list(eachreport)
        finalarray.append(eachrowsplit)
    print(finalarray)
    
    #first we need to find the gaurd
    for rowid, row in enumerate(finalarray):
        for charid, char in enumerate(row):
            if char == '^':
                gaurdlocation = (charid,rowid)
                gaurdx = charid
                gaurdy= rowid
                
    visited =[gaurdlocation]
    print(gaurdx)
    print(gaurdy)
    
    completedpath = movegaurd(finalarray, gaurdx, gaurdy, visited)
    print(completedpath)
    xcount = 0
    
    for row in completedpath:
        rowcount = row.count('X')
        xcount = xcount + rowcount
    xcount += 1
    print(xcount)
    
    

    
    

def movegaurd(array, gaurdx, gaurdy, visited):
    while True:
        #up
        #now we check which direction the gaurd wants to move in
        if array[gaurdy][gaurdx] == '^':
            #check if we are at the edge of the grid
            if gaurdy == 0:
                return array
            #check if we are at an obstacle:
            if array[gaurdy-1][gaurdx] == '#':
                array[gaurdy][gaurdx] = '>'
                continue
            #at this point we can move
            char = array[gaurdy][gaurdx]
            array[gaurdy][gaurdx] = 'X'
            gaurdy -= 1
            array[gaurdy][gaurdx] = '^'
            newvisited = (gaurdx,gaurdy)
            visited.append(newvisited)
        
        #left
        #now we check which direction the gaurd wants to move in
        if array[gaurdy][gaurdx] == '>':
            #check if we are at the edge of the grid
            if gaurdx == len(array[:-1]):
                return array
            #check if we are at an obstacle:
            if array[gaurdy][gaurdx+1] == '#':
                array[gaurdy][gaurdx] = 'v'
                continue
            #at this point we can move
            char = array[gaurdy][gaurdx]
            array[gaurdy][gaurdx] = 'X'
            gaurdx += 1
            array[gaurdy][gaurdx] = '>'
            newvisited = (gaurdx,gaurdy)
            visited.append(newvisited)
        
        #down
        #now we check which direction the gaurd wants to move in
        if array[gaurdy][gaurdx] == 'v':
            #check if we are at the edge of the grid
            if gaurdy == len(array[:-1]):
                return array
            #check if we are at an obstacle:
            if array[gaurdy+1][gaurdx] == '#':
                array[gaurdy][gaurdx] = '<'
                continue
            #at this point we can move
            char = array[gaurdy][gaurdx]
            array[gaurdy][gaurdx] = 'X'
            gaurdy += 1
            array[gaurdy][gaurdx] = 'v'
            newvisited = (gaurdx,gaurdy)
            visited.append(newvisited)
        
        #right
        #now we check which direction the gaurd wants to move in
        if array[gaurdy][gaurdx] == '<':
            #check if we are at the edge of the grid
            if gaurdx == 0:
                return array
            #check if we are at an obstacle:
            if array[gaurdy][gaurdx-1] == '#':
                array[gaurdy][gaurdx] = '^'
                continue
            #at this point we can move
            char = array[gaurdy][gaurdx]
            array[gaurdy][gaurdx] = 'X'
            gaurdx -= 1
            array[gaurdy][gaurdx] = '<'
            newvisited = (gaurdx,gaurdy)
            visited.append(newvisited)        
        
    
        
        #print(array)
            
        


f = open("input.txt", "r")
input = str(f.read())

gaurds(input)