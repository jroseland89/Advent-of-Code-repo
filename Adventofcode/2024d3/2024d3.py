# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:56:15 2024

@author: Jrose
"""

def mullitover(instructions):
    mullistposition = []
    index = 0
    #while loop to create a list to find 'mul(' index locations in the instructions
    while index < len(instructions):
        index = instructions.find('mul(', index)
        if index == -1:
            break
        mullistposition.append(index)
        index += 4
    
    listofmuls1 = []
    listofmuls2 = []
    validchars = ',)0123456789'
    validnums = '0123456789'
    for eachmul in mullistposition:
        #need to check if each mul is 'valid' by sequencing through the chars
        #for 0123456789*) only
        validcounter = 4
        mulposition = 0
        while True:
            if instructions[eachmul+validcounter] not in validchars:
                break
            if instructions[eachmul+validcounter] in validnums:
                validcounter += 1
                continue
            if instructions[eachmul+validcounter] == ',':
                mulposition = validcounter
                validcounter += 1
                continue
            #at this point the char must be a ')'
            listofmuls1.append(instructions[eachmul+4:eachmul+mulposition])
            listofmuls2.append(instructions[eachmul+mulposition+1:eachmul+validcounter])
            break
    
    #now mulitply each set of values together
    counter = 0
    score = 0
    for entry in listofmuls1:
        score = score + (int(entry) * int(listofmuls2[counter]))
        counter += 1
    return score

def mullitoverdo(instructions):
    #find index location of the string 'do' and 'don't'
    dolistposition = []
    index = 0
    while index < len(instructions):
        index = instructions.find('do', index)
        if index == -1:
            break
        dolistposition.append(index)
        index += 2
    dontlistposition = []
    index = 0
    while index < len(instructions):
        index = instructions.find("don't", index)
        if index == -1:
            break
        dontlistposition.append(index)
        index += 5
    #since 'do' appears within 'don't', we remove the instances of 'don't' from
    #within the 'do' list
    for item in dolistposition:
        if item in dontlistposition:
            dolistposition.remove(item)
    
    #now we alter the instructions so to only append chars when 'do' was the most
    #recently seen condition
    newinstructions = ''
    do = True
    index = 0
    for char in instructions:
        if index in dolistposition:
            do = True
        if index in dontlistposition:
            do = False
        if do == True:
            newinstructions = newinstructions + char
        index += 1
    #now run the standard mullitover function with the new instructions
    return mullitover(newinstructions)
            
        
testcase = "mul(1,1)don'thellodoblah"

f = open("instructions.txt", "r")
instructions = str(f.read())

print(mullitover(instructions))
print(mullitoverdo(instructions))