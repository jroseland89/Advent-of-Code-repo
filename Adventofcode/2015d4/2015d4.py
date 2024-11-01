# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:49:13 2024

@author: Jrose
"""

import hashlib

def AdventCoins(puzzleinput,zeros):
    """
    Returns: the secret key number that results in the first X digits of the
    MD5 hash to be zero, with X being determined by the 'zeros' input.
    The string hashed is the puzzle input + secret key number
    """
    codecounter = 0 #start the secret key counter
    while True:
        puzzlekey = puzzleinput + str(codecounter) #sets the key to be hashed
        hexiresult = hashlib.md5(puzzlekey.encode()) #returns the hexidecimal hash
        zerosstring = str('0' * zeros) #calculates the number of zeros to check
        #if statement to check the result and return the secret key if true
        if str(hexiresult.hexdigest()[0:zeros]) == zerosstring:
            return codecounter
        codecounter += 1 #increase count and repeat loop
            

puzzleinput = 'iwrupvqb'

print(AdventCoins(puzzleinput, 6))