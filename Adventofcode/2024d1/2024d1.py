# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 08:05:53 2024

@author: Jrose
"""

def listhelper(textinput):
    """
    Helper function to bring in the text input from AoC, then split out into each
    list based on if it is an odd or even position in the list.
    """
    bothlists = textinput.split()
    
    leftlist = []
    rightlist = []
    listposition = 0
    for item in bothlists:
        if listposition % 2 == 0:
            leftlist.append(item)
        else:
            rightlist.append(item)
        listposition += 1
    return leftlist, rightlist
    
def locationIDs(textinput):
    """
    Sorts the two lists and then finds the absolute difference between each
    adjacent pair and sums these differences
    """
    leftlist, rightlist = listhelper(textinput)
    
    listposition = 0
    leftlist.sort()
    rightlist.sort()
    listsum = 0
    
    for item in leftlist:
        listsum = listsum + abs(int(item) - int(rightlist[listposition]))
        listposition += 1
    
    return listsum
        
def locationIDsharder(textinput):
    """
    For each item in the left list, it finds the number of occurances of that value
    in the right list. The left list value is then multiplied by the number of
    occurances. These scores are then summed for all left list values.
    """
    leftlist, rightlist = listhelper(textinput)
    
    listscore = 0
    numberofappears = 0
    
    for leftitem in leftlist:
        #for each item in leftlist we need to find the number of occurances
        #in the right list, so we need another loop
        for rightitem in rightlist: #this loop finds the number of occurances
            if leftitem == rightitem:
                numberofappears += 1
        leftitemscore = int(leftitem) * numberofappears
        listscore = listscore + leftitemscore
        numberofappears = 0
    return listscore
                    
f = open("comparelists.txt", "r")
directions = str(f.read())

print(locationIDs(directions))
print(locationIDsharder(directions))