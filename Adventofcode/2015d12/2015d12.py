# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 12:07:46 2024

@author: Jrose
"""

def findnumbersandsum(inputstring):
    """
    Returns: the sum of all numperical values within the input string,
    starting a new number whenever a non-numerical value is found
    """
    totalsum = 0
    currentnumber = ''
    isanumber = '1234567890-' # minus sign (-) needs to be included to identify -ve numbers
    #this for loop finds indivisual numbers and adds them to a sum value
    for char in inputstring:
        if str(char) in isanumber:
            currentnumber = str(currentnumber) + str(char)
        else:
            #this nested if statement finds out if there is a number stored when
            #a non-numerical char is found. it only tries to add a number to the
            #sum if it is the first non-numperical char after a number
            if currentnumber == '':
                continue
            else:
                totalsum = totalsum + int(currentnumber)
                currentnumber = ''
    return totalsum

#inputstring = str([1,2,3])

f = open("jsonastext.txt", "r")
inputstring = str(f.read())

print(findnumbersandsum(inputstring))
                
        