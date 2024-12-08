# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:27:06 2024

@author: Jrose
"""
from itertools import permutations
distances = [['Tristram', 'AlphaCentauri', 34],
['Tristram', 'Snowdin', 100],
['Tristram', 'Tambi', 63],
['Tristram', 'Faerun', 108],
['Tristram', 'Norrath', 111],
['Tristram', 'Straylight', 89],
['Tristram', 'Arbre', 132],
['AlphaCentauri', 'Snowdin', 4],
['AlphaCentauri', 'Tambi', 79],
['AlphaCentauri', 'Faerun', 44],
['AlphaCentauri', 'Norrath', 147],
['AlphaCentauri', 'Straylight', 133],
['AlphaCentauri', 'Arbre', 74],
['Snowdin', 'Tambi', 105],
['Snowdin', 'Faerun', 95],
['Snowdin', 'Norrath', 48],
['Snowdin', 'Straylight', 88],
['Snowdin', 'Arbre', 7],
['Tambi', 'Faerun', 68],
['Tambi', 'Norrath', 134],
['Tambi', 'Straylight', 107],
['Tambi', 'Arbre', 40],
['Faerun', 'Norrath', 11],
['Faerun', 'Straylight', 66],
['Faerun', 'Arbre', 144],
['Norrath', 'Straylight', 115],
['Norrath', 'Arbre', 135],
['Straylight', 'Arbre', 127]]

stars = ['Tristram', 'AlphaCentauri', 'Snowdin', 'Tambi', 'Faerun', 'Norrath', 'Straylight', 'Arbre']
best = 100000000
worst = 0
allroutes = list(permutations(stars))
for eachroute in allroutes:
    travelled = 0
    for index, eachstar in enumerate(eachroute[:-1]):
        for possibledistances in distances:
            #print(possibledistances)
            if (eachstar in possibledistances) and (eachroute[index+1] in possibledistances):
                travelled += int(possibledistances[2])
    print(eachroute)
    if travelled <= best:
        best = travelled
    if travelled >= worst:
        worst = travelled
print(best)
print(worst)
                
    