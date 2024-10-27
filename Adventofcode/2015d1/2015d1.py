# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:30:59 2024

@author: Jrose
"""

def santastairs(floorinstructions):
    """
    Returns: the final floor santa lands on at the end of the string
    """
    floor = 0
    for eachfloor in floorinstructions:
        if eachfloor == '(':
            floor += 1
        if eachfloor == ')':
            floor -= 1
    return floor

def santainbasement(floorinstructions):
    """
    Returns: the position of the character that causes santa to visit the basement
    """
    charposition = 1
    floor = 0
    for eachfloor in floorinstructions:
        if eachfloor == '(':
            floor += 1
        if eachfloor == ')':
            floor -= 1
        if floor < 0:
            return charposition
        charposition += 1



f = open("santa.txt", "r")
floorinstructions = str(f.read())

#floorinstructions = '()())'

print(santastairs(floorinstructions))

print(santainbasement(floorinstructions))

