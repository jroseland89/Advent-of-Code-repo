# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:09:23 2024

@author: Jrose
"""
def bridgerepair(inputtext):
    #split both inputs into lists:
    array = (inputtext.splitlines()) #split the input into a list entry per line / report
    finalarray = []
    for eachreport in array: #split each line / report into individual sub-lists with an entry per level
        eachrowsplit = eachreport.split()
        finalarray.append(eachrowsplit)
        
    #print(finalarray)
    #get the first 'result' term    
    testresult = []
    for eachrow in finalarray:
        testresult.append(eachrow[0])
    #print (testresult)
    
    testresultvalue = []
    for eachvalue in testresult:
       testresultvalue.append(eachvalue[:-1])
    #print(testresultvalue)
    
    
    #now test if each value can be summed or multiplied
    totalsum = 0
    for reportindex, eachreport in enumerate(finalarray):
        correctresult = permutationscalc(testresultvalue[reportindex], eachreport[1:])
        print(correctresult)
        totalsum += correctresult
    print(totalsum)
        
            
def permutationscalc(result, values):
    operatorlength = len(values) -1
    operator = '+' * operatorlength
    
    #for valueid, value in enumerate(values[1:]):
        #operator.append('+')
    
    while True:
        calculation = int(values[0])
        for valueid, value in enumerate(values[1:]):
            if operator[valueid] == '+':
                calculation += int(value)
                
            if operator[valueid] == '*':
                calculation = calculation * int(value) 
                
            if operator[valueid] == '|':
                concatenation = str(calculation) + str(value)
                calculation = int(concatenation)
                #print(calculation)
        if calculation == int(result):
            #print('result' + str(calculation))
            return calculation
        
        passwordlength = len(operator)
        overflowcase = passwordlength * '*'
        if operator == overflowcase:
            return 0
        operator = increments2(operator, operatorlength)
        
        
        
        '''
            
        if operator[position] == '+':
            operator[position] = '*'
            continue
        else:
            operator[position] = '+'
            position = +1
            #print(position)
        '''

def increments(password, length):
    """
    Returns: an increment of the password. Passwords are composed of eight lowercase
    letters not including i, o or l. 
    """
    passwordchar = password[length-1] #tracks the password char being incremented
    
    if passwordchar == '*':
        newpasswordchar = '+'
        #if the tracked char is z the function is called recursively for the next
        #char to the left in the password
        #if length == len(password):
            #print('overflow')
            #return 'overflow'
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        return increments(newpassword, length - 1)
    

    
    if passwordchar == '+':
        newpasswordchar = '*'
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        
    return (newpassword)
                
def increments2(password, length):
    """
    Returns: an increment of the password. Passwords are composed of eight lowercase
    letters not including i, o or l. 
    """
    passwordchar = password[length-1] #tracks the password char being incremented
    
    if passwordchar == '*':
        newpasswordchar = '+'
        #if the tracked char is z the function is called recursively for the next
        #char to the left in the password
        #if length == len(password):
            #print('overflow')
            #return 'overflow'
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
        return increments2(newpassword, length - 1)
    
    if passwordchar == '+':
        newpasswordchar = '|'
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
    if passwordchar == '|':
        newpasswordchar = '*'
        newpassword = (password[:length - 1] + newpasswordchar + password[length:])
    #print(newpassword)
    return (newpassword)



f = open("ninput.txt", "r")
inputtext = str(f.read())

bridgerepair(inputtext)
#permutationscalc(7290,[6,8,6,15])
#increments2('++*', 3)