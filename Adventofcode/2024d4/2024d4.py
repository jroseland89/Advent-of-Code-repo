# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 07:34:02 2024

@author: Jrose
"""
def findwords(wordsearch):
    array = wordsearch.splitlines()
    #findwordsgoingforward
    forwards = 0
    for row in array:
        hindex = 0
        while hindex < len(row):
            hindex = row.find('XMAS', hindex)
            if hindex == -1:
                break
            forwards +=1
            hindex += 1

    #findwordsgoingbackwards
    backwards = 0
    for row in array:
        hindex = 0
        while hindex < len(row):
            hindex = row.find('SAMX', hindex)
            if hindex == -1:
                break
            backwards +=1
            hindex += 1
    
    #findforwardsvertical
    forvertical = 0
    vindex = 0
    for row in array:
        hindex = 0
        for char in row:
            if char != 'X':
                hindex += 1
                continue
            if array[vindex+1][hindex] != 'M':
                hindex += 1
                continue
            if array[vindex+2][hindex] != 'A':
                hindex += 1
                continue
            if array[vindex+3][hindex] != 'S':
                hindex += 1
                continue
            forvertical += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
    #findbackwardsvertical
    vindex = 0
    backvertical = 0
    for row in array:
        hindex = 0
        for char in row:
            if char != 'S':
                hindex += 1
                continue
            if array[vindex+1][hindex] != 'A':
                hindex += 1
                continue
            if array[vindex+2][hindex] != 'M':
                hindex += 1
                continue
            if array[vindex+3][hindex] != 'X':
                hindex += 1
                continue
            backvertical += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
    
    #find forwarddown diag
    vindex = 0
    forwarddown = 0
    for row in array:
        hindex = 0
        for char in row:
            if hindex >= 137:
                break
            if char != 'X':
                hindex += 1
                continue
            if array[vindex+1][hindex+1] != 'M':
                hindex += 1
                continue
            if array[vindex+2][hindex+2] != 'A':
                hindex += 1
                continue
            if array[vindex+3][hindex+3] != 'S':
                hindex += 1
                continue
            forwarddown += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
    
    #find backwarddown diag
    vindex = 0
    backwarddown = 0
    for row in array:
        hindex = 0
        for char in row:
            if hindex < 0:
                hindex +=1
                continue
            if char != 'X':
                hindex += 1
                continue
            if array[vindex+1][hindex-1] != 'M':
                hindex += 1
                continue
            if array[vindex+2][hindex-2] != 'A':
                hindex += 1
                continue
            if array[vindex+3][hindex-3] != 'S':
                hindex += 1
                continue
            backwarddown += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
    
    
    #find reversedown diag
    vindex = 0
    forwarddown = 0
    for row in array:
        hindex = 0
        for char in row:
            if hindex >= 137:
                break
            if char != 'S':
                hindex += 1
                continue
            if array[vindex+1][hindex+1] != 'A':
                hindex += 1
                continue
            if array[vindex+2][hindex+2] != 'M':
                hindex += 1
                continue
            if array[vindex+3][hindex+3] != 'X':
                hindex += 1
                continue
            forwarddown += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
    
    #find reverseback diag
    vindex = 0
    backwarddown = 0
    for row in array:
        hindex = 0
        for char in row:
            if hindex <= 0:
                hindex += 1
                continue
            if char != 'S':
                hindex += 1
                continue
            if array[vindex+1][hindex-1] != 'A':
                hindex += 1
                continue
            if array[vindex+2][hindex-2] != 'M':
                hindex += 1
                continue
            if array[vindex+3][hindex-3] != 'X':
                hindex += 1
                continue
            backwarddown += 1
            hindex += 1
        vindex +=1
        if vindex >= 137:
            break
        
    
    print(forwards)
    print(backwards)
    print(forvertical)
    print(backvertical)
    print(forwarddown)
    print(backwarddown)
    sumall = forwards + backwards + forvertical + backvertical + forwarddown + backwarddown
    print(sumall)


f = open("xmas.txt", "r")
wordsearch = str(f.read())

testcase = ['MMMSXXMASM',
'MSAMXMSMSA',
'AMXSXMAAMM',
'MSAMASMSMX',
'XMASAMXAMM',
'XXAMMXXAMA',
'SMSMSASXSS',
'SAXAMASAAA',
'MAMMMXMMMM',
'MXMXAXMASX',]

findwords(wordsearch)