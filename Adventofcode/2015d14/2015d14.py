# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:46:48 2024

@author: Jrose
"""

def reindeerolympics(reindeerattributes, time):
    speed = reindeerattributes[0]
    stamina = reindeerattributes[1]
    rest = reindeerattributes[2]
    
    #calculate full cycles
    fullcycles = time // (stamina + rest)
    distance = fullcycles * speed * stamina
    
    #calculate distance of remainder
    remainder = time % (stamina + rest)
    
    if remainder >= stamina:
        distance = distance + (speed * stamina)
    else:
        distance = distance + (speed * remainder)
    return distance
    
def improvedreindeerolypics(time):
    Rudolph = [22 , 8 , 165]
    Cupid = [8 , 17 , 114]
    Prancer = [18 , 6 , 103]
    Donner = [25 , 6 , 145]
    Dasher = [11 , 12 , 125]
    Comet = [21 , 6 , 121]
    Blitzen = [18 , 3 , 50]
    Vixen = [20 , 4 , 75 ]
    Dancer = [7 , 20 , 119]
    currenttime = 1
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    r7 = 0
    r8 = 0
    r9 = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    while currenttime <= time:
        r1 = reindeerolympics(Rudolph, currenttime)
        r2 = reindeerolympics(Cupid, currenttime)
        r3 = reindeerolympics(Prancer, currenttime)
        r4 = reindeerolympics(Donner, currenttime)
        r5 = reindeerolympics(Dasher, currenttime)
        r6 = reindeerolympics(Comet, currenttime)
        r7 = reindeerolympics(Blitzen, currenttime)
        r8 = reindeerolympics(Vixen, currenttime)
        r9 = reindeerolympics(Dancer, currenttime)
        roundresult = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
        roundresult.sort()
        roundwinner = roundresult[8]
        if roundwinner == r1:
            s1 += 1
        if roundwinner == r2:
            s2 += 1
        if roundwinner == r3:
            s3 += 1
        if roundwinner == r4:
            s4 += 1
        if roundwinner == r5:
            s5 += 1
        if roundwinner == r6:
            s6 += 1
        if roundwinner == r7:
            s7 += 1
        if roundwinner == r8:
            s8 += 1
        if roundwinner == r9:
            s9 += 1
        currenttime += 1
    finalresult = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    print(finalresult)
    finalresult.sort()
    finalwinner = finalresult[8]
    return finalwinner



#reindeerattrubutes - speed,stamina,rest period
#comet = [14, 10, 127]

Rudolph = [22 , 8 , 165]
Cupid = [8 , 17 , 114]
Prancer = [18 , 6 , 103]
Donner = [25 , 6 , 145]
Dasher = [11 , 12 , 125]
Comet = [21 , 6 , 121]
Blitzen = [18 , 3 , 50]
Vixen = [20 , 4 , 75 ]
Dancer = [7 , 20 , 119]

allreindeer = [Rudolph,Cupid,Prancer,Donner,Dasher,Comet,Blitzen,Vixen,Dancer]


print('Rudolph ' + str(reindeerolympics(Rudolph, 2503)))
print('Cupid ' + str(reindeerolympics(Cupid, 2503)))
print('Prancer ' + str(reindeerolympics(Prancer, 2503)))
print('Donner ' + str(reindeerolympics(Donner, 2503)))
print('Dasher ' + str(reindeerolympics(Dasher, 2503)))
print('Comet ' + str(reindeerolympics(Comet, 2503)))
print('Blitzen ' + str(reindeerolympics(Blitzen, 2503)))
print('Vixen ' + str(reindeerolympics(Vixen, 2503)))
print('Dancer ' + str(reindeerolympics(Dancer, 2503)))

print(improvedreindeerolypics(2503))