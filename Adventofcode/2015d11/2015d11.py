# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:37:32 2024

@author: Jrose
"""

import string


def incrementpass(password, length):
    """
    Returns: an increment of the password. Passwords are composed of eight lowercase
    letters not including i, o or l. 
    """
    availableletters = 'abcdefghjkmnpqrstuvwxyz' #i, o and l are excluded at this stage
    #to increase computation speed
    passwordchar = password[length-1] #tracks the password char being incremented
    
    if passwordchar == 'z':
        newpasswordchar = 'a'
        #if the tracked char is z the function is called recursively for the next
        #char to the left in the password
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        return incrementpass(newpassword, length - 1)
    
    letternumber = 0 #keeps track of which letter the for loop is comparing against
    
    for letter in availableletters:

        if passwordchar == letter:
            #char is now incremented by one
            newpasswordchar = availableletters[(letternumber+1)]
            newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        letternumber +=1
        
    return (newpassword)

def corporatepolicy(password,length):
    """
    Returns: increments the initial password until one is found that meets the test
    criteria.
    """
    lowercasestring = string.ascii_lowercase
    while True:
        test1 = False #test1 looks for three increasing consecutive letters
        test2 = False #test2 looks for at least two different, non-overlapping
        #pairs of letters
        
        #This first loop sees if test1 is true
        charcounter = 0
        for char in password[:length - 2]:
            charstring = password[charcounter:charcounter+3]
            if charstring in lowercasestring:
                test1 = True
            charcounter += 1
            
        #this second loop sees if test2 is true by adding unique consecutive
        #pairs of letters to a list, and checking if there are at least
        #two values in the list
        doubleletterlist = []
        doubleletterlist.clear()
        charcounter = 0
        for char in password[:length - 1]:
            if char == password[charcounter + 1]:
                if char not in doubleletterlist:
                    doubleletterlist.append(char)
            charcounter += 1
        if len(doubleletterlist) >= 2:
            test2 = True
        
        #check if both tests are true, if so return valid password
        if (test1 == True and test2 == True):
            return password
        
        #if the tests are not met, increment the password
        password = incrementpass(password, length)
    
            
    
print(corporatepolicy('hepxxzaa', 8))
        
    