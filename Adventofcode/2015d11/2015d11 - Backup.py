# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:37:32 2024

@author: Jrose
"""

import string


def incrementpass(password, length):
    availableletters = 'abcdefghjkmnpqrstuvwxyz'
    passwordchar = password[length-1]
    letternumber = 0
    for letter in availableletters:
        if passwordchar == 'z':
            newpasswordchar = 'a'
            newpassword = (password[:length - 1] + newpasswordchar + password[length:])
            return incrementpass(newpassword, length - 1)
        if passwordchar == letter:
            newpasswordchar = availableletters[(letternumber+1)]
            newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        letternumber +=1
    return (newpassword)

def corporatepolicy(password,length):
    while True:
        test1 = False
        test2 = False
        lowercasestring = string.ascii_lowercase
        
        charcounter = 0
        for char in password[:length - 2]:
            charstring = password[charcounter:charcounter+3]
            if charstring in lowercasestring:
                test1 = True
            charcounter += 1
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
        if (test1 == True and test2 == True):
            return password
        password = incrementpass(password, length)
    
            
    


print(corporatepolicy('hepxxzaa', 8))
        
    