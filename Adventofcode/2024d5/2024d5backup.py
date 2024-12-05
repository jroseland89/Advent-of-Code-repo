# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:05:16 2024

@author: Jrose
"""
def printqueue(updates, ordering):
    #split both inputs into lists:
        updatelist = updates.splitlines()
        orderlist = ordering.splitlines()
        finallist = []
        for eachupdate in updatelist: #split each line / report into individual sub-lists with an entry per level
            eachrowint = [int(x) for x in eachupdate.split(',')]
            finallist.append(eachrowint)

    
        #rightorderindex=[]
        goodlist = list(finallist)
        
        #now a loop to look to see if each update is correct, and if it is append it to a list
        for updateid, update in enumerate(finallist):
            state = True
            #now we work through each item in the update
            for valueid, value in enumerate(update):
                
                #print(update)
                #now we look to see if each item incrementing from the value is in the list:
                for valueid2, value2 in enumerate(update):
                    if valueid == valueid2:
                        continue
                    #print(str(value)+'|'+str(value2))
                    if valueid < valueid2:
                        if str(value2)+'|'+str(value) in orderlist:
                            #print(str(value2)+'|'+str(value))
                            state = False
                            goodlist.remove(update)
                            break
                    if valueid > valueid2:
                        if str(value)+'|'+str(value2) in orderlist:
                            #print(str(value)+'|'+str(value2))
                            state = False
                            goodlist.remove(update)
                            break
                if state == False:
                    break
                       
        #print(goodlist)
        score = 0
        for goodupdate in goodlist:
            middlevalue = int(len(goodupdate)/2)                          
            score = score + goodupdate[middlevalue]
        #print(score)
        return(finallist, goodlist, orderlist)

def printqueue2(updates, ordering):
    finallist, goodlist, orderlist = printqueue(updates, ordering)
    badlist = list(finallist)
    for item in finallist:
        if item in goodlist:
            badlist.remove(item)
    #print(badlist)
    correctedlist =[]
    done = 0
    for updateid, update in enumerate(badlist):
        correctedupdate = swaporder(update,orderlist)
        done+=1
        print(done)
        
        correctedlist.append(correctedupdate)
    print(correctedlist)
    score = 0
    for goodupdate in goodlist:
        middlevalue = int(len(goodupdate)/2)                          
        score = score + goodupdate[middlevalue]
    print(score)


def swaporder(update,orderlist):  
    for valueid, value in enumerate(update):
        #print(update)
        #now we look to see if each item incrementing from the value is in the list:
        for valueid2, value2 in enumerate(update):
            if valueid == valueid2:
                continue
            #print(str(value)+'|'+str(value2))
            if valueid < valueid2:
                if str(value2)+'|'+str(value) in orderlist:
                    #we now need to swap the values
                    
                    temp = update[valueid]
                    update[valueid] = update[valueid2]
                    update[valueid2] = temp
                    print(update)
                    swaporder(update,orderlist)
            elif valueid > valueid2:
                if str(value)+'|'+str(value2) in orderlist:
                    temp = update[valueid2]
                    update[valueid2] = update[valueid]
                    update[valueid] = temp
                    print(update)
                    swaporder(update,orderlist)

    return update
                            
                
    


f = open("updates.txt", "r")
updates = str(f.read())

f = open("ordering.txt", "r")
ordering = str(f.read())

printqueue2(updates, ordering)