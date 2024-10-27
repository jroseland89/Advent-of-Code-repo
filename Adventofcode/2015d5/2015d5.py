# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:47:20 2024

@author: Jrose
"""

def naughtyornice(naughtyornicelist):
    '''
    returns the number of nice strings in the list
    '''
    nicestrings = 0
    for string in naughtyornicelist[0]:
        #reset test status (test1 & test2 need to be proved true, test3 can only be proved false)
        test1 = False #tests to find at least 3 vowels
        test2 = False #tests to find at least one double letter
        test3 = True #is false if 'bad' strings ab, cd, pq, or xy appear
        vowelcount = 0 
        if string[0] == 'a' or string[0] == 'e' or string[0] == 'i' \
        or string[0] == 'o' or string[0] == 'u':
            vowelcount += 1 #reports if the first char in a string is a vowel
        
        stringcounter = 1 #keeps track of the char position in the string for loop
        for char in string[1:]:
            if char == 'a' or char == 'e' or char == 'i' \
            or char == 'o' or char == 'u':
                vowelcount += 1 #keeps count of vowels
            if char == string[stringcounter-1]:
                test2 = True # tests if there is a double letter
            if char == 'b' and string[stringcounter-1] == 'a':
                test3 = False #series of tests to see if 'bad' strings appear
            if char == 'd' and string[stringcounter-1] == 'c':
                test3 = False
            if char == 'q' and string[stringcounter-1] == 'p':
                test3 = False
            if char == 'y' and string[stringcounter-1] == 'x':
                test3 = False
            stringcounter += 1
        if vowelcount >= 3:
            test1 = True #tests if there are at least 3 vowels
        if (test1 == True and test2 == True and test3 == True):
            nicestrings += 1 #all 3 tests must be met for it to be a nice string
    return nicestrings

def improvednaughtyornice(naughtyornicelist):
    nicestrings = 0
    for string in naughtyornicelist[0]:
        #reset test status
        test1a = False #tests to find any two letters that appear twice
        test1b = True #tests if the pair of letters overlap
        test2 = False #tests to find at least one letter which repeats with exactly one letter between
        stringcounter = 0
        adjacentpairs = []
        for char in string:
            #test1a - build a list of adjacent pared letters
            if stringcounter >= 1:
                adjacentpairs.append(string[stringcounter-1] + char)
            #test2 - check if at least one letter repeats with one letter between
            if stringcounter >= 2:
                if char == string[stringcounter-2]:
                    test2 = True
            stringcounter += 1
                
        #loop to test 1b with adjacentpairs list
        paircounter = 1
        for pair in adjacentpairs[1:]:
            if pair == adjacentpairs[paircounter-1]:
                test1b = False
            paircounter += 1
        #check to see if there are duplicates in the list for test1a
        setpairs = set(adjacentpairs)
        if len(adjacentpairs) != len(setpairs):
            test1a = True
    
        if (test1a == True and test1b == True and test2 == True):
            nicestrings += 1 #all tests must be met for it to be a nice string    
    return nicestrings        
            


#naughtyornicelist = ['ugknbfddgicrmopn','aaa','jchzalrnumimnmhp','haegwjzuvuyypxyu','dvszwmarrgswjxmb']

#naughtyornicelist = [['qjhvhtzxzqqjkmpb','xxyxx','uurcxstgmygtbstg','ieodomkazucvgmuy']]
'''
read file and split each line into an item within a list
'''
f = open("naughtyornicelist.txt", "r")
presentcontent = f.read()
f.close()
groups = presentcontent.split("\n\n")
naughtyornicelist = [group.split("\n") for group in groups ]




#print(naughtyornice(naughtyornicelist))

print(improvednaughtyornice(naughtyornicelist))
