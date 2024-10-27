# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:51:06 2024

@author: Jrose
"""

def elveslookelvessay(sequence,depth):
    '''
    recursive function that returns the length of chars in the elve game result.
    For each iteration, the game records the number of occurences of a char + that char
    '''
    charcounter = 0 
    identicalchars = 1
    newsequence = ''
    for char in sequence:
        #This first edge case if statement is for the last char in the sequence
        if charcounter + 1 == len(sequence):
            newsequence = newsequence + str(identicalchars) + char
            identicalchars = 1
            break
        #This if statement logs the number of occurences of a char in sequence
        if char == sequence[charcounter + 1]:
            identicalchars += 1
        #The else statement appends the number of occurences + that char, and resets the identicalcharcounter
        else:
            newsequence = newsequence + str(identicalchars) + char
            identicalchars = 1
        charcounter += 1
    sequence = newsequence
    # if depth is 1 this is the last iteration and the result can be returned
    if depth == 1:
        return len(sequence)
    #if depth is greater than 1 the game iterates the next recursion by reducing
    #the depth counter and calling the function again with this iteration's result
    print(depth)
    depth -= 1
    return elveslookelvessay(sequence, depth)
            
sequence = '1321131112'

print(elveslookelvessay(sequence, 50))

        
    
