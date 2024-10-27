# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:20:17 2024

@author: Jrose
"""

def santapresentdelivery(directions):
    """
    Returns: the number of houses santa visits on his direction instructions
    """
    housesvisited = ['0E0N']
    E = 0 #sets initial easting co-ords
    N = 0 #sets initial northin co-ords
    for house in directions:
        if house == '^': #updates easting and northing co-ords
            N += 1
        if house == 'v':
            N -= 1
        if house == '>':
            E += 1
        if house == '<':
            E -= 1
        #create a string with the co-ordinate address and add it to
        #the list if it has not been visited before
        houseaddress = (str(E) + 'E' + str(N) + 'N')
        if houseaddress not in housesvisited:
            housesvisited.append(houseaddress)
    #return the number of houses (the length of the visited houses list)
    return len(housesvisited)


def santaandrobotsantaarecrapatteamwork(directions):
    """
    First find the list of houses santa visits. As above but only even instructions
    """
    housesvisited = ['0E0N']
    E = 0 #sets initial easting co-ords
    N = 0 #sets initial northin co-ords
    for house in directions[::2]:
        if house == '^': #updates easting and northing co-ords
            N += 1
        if house == 'v':
            N -= 1
        if house == '>':
            E += 1
        if house == '<':
            E -= 1
        #create a string with the co-ordinate address and add it to
        #the list if it has not been visited before
        houseaddress = (str(E) + 'E' + str(N) + 'N')
        if houseaddress not in housesvisited:
            housesvisited.append(houseaddress)
    """
    Now robo-santa does all the odd instructions
    """   
    E = 0 #sets initial easting co-ords
    N = 0 #sets initial northin co-ords
    for house in directions[1::2]:
        if house == '^': #updates easting and northing co-ords
            N += 1
        if house == 'v':
            N -= 1
        if house == '>':
            E += 1
        if house == '<':
            E -= 1
        #create a string with the co-ordinate address and add it to
        #the list if it has not been visited before
        houseaddress = (str(E) + 'E' + str(N) + 'N')
        if houseaddress not in housesvisited:
            housesvisited.append(houseaddress)
    return len(housesvisited) #returns the number of houses that get at least one present

#directions = '^v^v^v^v^v'

f = open("directions.txt", "r")
directions = str(f.read())

print(santapresentdelivery(directions))

print(santaandrobotsantaarecrapatteamwork(directions))

    