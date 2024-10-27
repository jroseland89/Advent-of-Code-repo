# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:54:56 2024

@author: Jrose
"""

def elvewrappingorder(presentlist):
    totalpresentarea = 0
    '''
    For some reason the list is in a list, so I need to return the first item
    within the outer list to get the inner list.
    
    Outer loop gets each present within the overal present list.
    Inner loop gets area of paper required for each present.
    '''
    for presents in presentlist[0]:
        l = ''
        h = ''
        w = ''
        xcount = 0
        for char in presents: 
            if char == 'x': #splits string into length, height and width
                xcount += 1
                continue
            if xcount == 0:
                l = l + char
            if xcount == 1:
                h = h + char
            if xcount == 2:
                w = w + char
        l = int(l) # need to convert l, h and t to integer values
        h = int(h)
        w = int(w)
        if( 2*l*w <= 2*w*h and 2*l*w <= 2*h*l):
            smallest = l*w # calculates smallest face for spare slack   
        if( 2*w*h <= 2*l*w and 2*w*h <= 2*h*l):
            smallest = w*h
        if( 2*h*l <= 2*l*w and 2*h*l <= 2*w*h):
            smallest = h*l
        presentarea = 2*l*w + 2*w*h + 2*h*l + smallest
        totalpresentarea = totalpresentarea + presentarea
    
    return totalpresentarea

            
def elveribbonorder(presentlist):
    totalbowlength = 0
    
    'as per the wrapping order, just with a different calculated output'
    
    for presents in presentlist[0]:
        l = ''
        h = ''
        w = ''
        xcount = 0
        for char in presents: 
            if char == 'x': #splits string into length, height and width
                xcount += 1
                continue
            if xcount == 0:
                l = l + char
            if xcount == 1:
                h = h + char
            if xcount == 2:
                w = w + char
        l = int(l) # need to convert l, h and t to integer values
        h = int(h)
        w = int(w)
        if (l+w <= l+h and l+w <= w+h):
            smallestperim = 2*(l+w) #calculates the smallest perimiter
        if (l+h <= l+w and l+h <= w+h):
            smallestperim = 2*(l+h)
        if (w+h <= l+h and w+h <= l+w):
            smallestperim = 2*(w+h)
        #bow length is defined by smallest perimeter plus present volume
        bowlength = smallestperim + (l*h*w)
        totalbowlength = totalbowlength + bowlength
        
    return totalbowlength
    
'''
read file and split each line into an item within a list
'''
f = open("presents.txt", "r")
presentcontent = f.read()
f.close()
groups = presentcontent.split("\n\n")
presentlist = [group.split("\n") for group in groups ]

#print(presentlist)
#presentlist = ['4x23x21', '22x29x19']

'''
call up result
'''

print(elvewrappingorder(presentlist))

print(elveribbonorder(presentlist))
