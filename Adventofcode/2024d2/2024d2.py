# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:09:09 2024

@author: Jrose
"""

def reactorsafereports(reports):
    """
    Function initially converts the .txt file into lists within a list, then
    adds to a counter if a report meets the criteria
    """
    array = reports.splitlines() #split the input into a list entry per line / report
    finalarray = []
    for eachreport in array: #split each line / report into individual sub-lists with an entry per level
        eachrowsplit = eachreport.split()
        eachrowasint = list(map(int, eachrowsplit)) #values as integers rather than strings
        finalarray.append(eachrowasint)

    safecounter = 0 #set a counter to record the safe reports
    #now we can find out if each report is acending or decending
    for eachreport in finalarray:
        acending = sorted(eachreport)
        decending = sorted(eachreport,reverse=True)

        if eachreport == acending or eachreport == decending:
            inrange = adjacentlevelshelper(eachreport)
            #if the report is acending or decending we use a helper function to
            #find out if the levels are close enough
            if inrange == True:
                safecounter += 1

    return safecounter


def adjacentlevelshelper(eachreport):
    """
    Runs through each level in a report and returns true if no adjacent values are
    equal or have a difference greater than 3
    """
    reportcounter = 0
    while reportcounter < len(eachreport) - 1:
        currentlevel = eachreport[reportcounter]
        nextlevel = eachreport[reportcounter + 1]
        if currentlevel == nextlevel:
            return False
        if abs(currentlevel-nextlevel) > 3:
            return False
        reportcounter +=1
    return True
            
def removelevel(eachreport,n):
    """
    For the second part, this helper function can remove a single level within a report
    """
    alteredreport = list(eachreport)
    alteredreport.pop(n)
    return alteredreport


def reactorsafereportsimproved(reports):
    """
    As per the initial function, but this time an additional loop is inserted that runs
    through each report with a level missing in turn
    """
    array = reports.splitlines() #split the input into a list entry per line / report
    finalarray = []
    for eachreport in array: #split each line / report into individual sub-lists with an entry per level
        eachrowsplit = eachreport.split()
        eachrowasint = list(map(int, eachrowsplit)) #values as integers rather than strings
        finalarray.append(eachrowasint)

    safecounter = 0 #set a counter to record the safe reports
    #now we can find out if each report is acending or decending
    for eachreport in finalarray:
        n = 0 #n sets the level position that we can try removing from the report
        while n < len(eachreport):
            #This loop cycles through each report with a level in position 'n'
            #removed to see if the conditions are met, otherwise it works as before
            alteredreport = removelevel(eachreport, n)
            acending = sorted(alteredreport)
            decending = sorted(alteredreport,reverse=True)
            if alteredreport == acending or alteredreport == decending:
                inrange = adjacentlevelshelper(alteredreport)
                #if the report is acending or decending we use a helper function to
                #find out if the levels are close enough
                if inrange == True:
                    safecounter += 1
                    break #break out of the while loop if the conditions are met to
                    #avoid double counting a single report
            n += 1 #if conditions are not met increment the level position to be removed

    return safecounter

#testcase = '1 1 3 4 11 7'

f = open("codes.txt", "r")
reports = str(f.read())

print(reactorsafereports(reports))
print(reactorsafereportsimproved(reports))