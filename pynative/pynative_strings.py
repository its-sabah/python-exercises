# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 11:30:36 2022

@author: AD676KL

Completing 'Python String Exercises'
source: https://pynative.com/python-exercises-with-solutions/
"""

#   Exercise 1A: Create a string made of the first, middle and last character
def slicer(str1):
    slen = len(str1)
    first = str1[0]
    last = str1[slen-1]
    middle = str1[int(slen/2)]
    str2 = first+middle+last
    print(str2)
slicer("tables")

#%%
#   Exercise 1B: Create a string made of the middle three characters
def middle3(str1):
    mid = int(len(str1)/2)
    str2 = str1[(mid-1):(mid+2)]
    print(str2)
    
middle3("JhonDipPeta")

#%%
#     Exercise 2: Append new string in the middle of a given string
def appendmid(s1, s2):
    s1a = s1[:(int(len(s1)/2))]
    s1b = s1[(int(len(s1)/2)):]
    s3 = s1a + s2 + s1b
    print(s3)

appendmid("Ault", "Kelly")

#%%
#   Exercise 3: Create a new string made of the first, middle, and last characters of each input string

def firstlast(s1, s2):
    s1 = s1[0]+s1[-1]
    s2 = s2[0]+s2[-1]
    s3 = s1+s2
    print(s3)

firstlast("America", "Japan")

#%%
#   Exercise 4: Arrange string characters such that lowercase letters should come first

def lowerfirst(s1):
    s1 = list(s1)
    s1lower = [i for i in s1 if i.islower()]
    s1upper = [i for i in s1 if i.isupper()]
    s2 = s1lower + s1upper
    s2 = "".join(s2)
    print(s2)

lowerfirst("HabbyPop")

#%%
#   Exercise 5: Count all letters, digits, and special symbols from a given string

def countchar(s1):
    s1 = list(s1)
    num=[]
    let=[]
    sym=[]
    for i in s1:
        i = str(i)
        if i.isnumeric() == True:
            num = num + list(i)
        elif i.isalpha() == True:
            let = let + list(i)
        else:
            sym = sym + list(i)
    print("number count:", len(num), " letter count:", len(let),
          "symbol count:", len(sym))
countchar("abs2^^")

#%%
#   Exercise 6: Create a mixed String using the following rules
def mixstr(s1, s2):
    s1list = list(s1)
    s2list = list(s2)
    s3=[]
    rems1, rems2 = 0,0
    if len(s1list) < len(s2list):
        maxlen = len(s1list)
        rems2 = len(s2list) - maxlen 
    else:
        maxlen = len(s2list)
        rems1 =  len(s1list) - maxlen
        
    for i in range(maxlen):
        s3 = s3 + list(s1[i]) + list(s2[-(i+1)])
        print(s3)
    if rems1 != 0:
        s3 = s3 + list(s1[rems1:])
    elif rems2 != 0:
        s3 = s3 + list(s2[rems2::-1])
    print("".join(s3))
mixstr("sabah", "tomi")

#%%

#   Exercise 7: String characters balance Test

def balancetest(s1, s2):
    if s1 in s2:
        print("True")
    else:
        print("False")
        
balancetest("hp", "hophi")


    
    
    
    
    
    
    
    
    