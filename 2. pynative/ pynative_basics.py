# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:52:40 2022

@author: AD676KL

Completing 'Python Basic Exercise for Beginners'
source: https://pynative.com/python-basic-exercise-for-beginners/
"""


#%%
#    Exercise 1: Calculate the multiplication and sum of two numbers


def sum_or_product(num1, num2):
    total = int(num1) * int(num2)
    if total > 1000:
        total = num1 + num2
    return total

print(sum_or_product(20, 30))
print(sum_or_product(30,40))

#%%

#   Exercise 2: Print the sum of the current number and the previous number
n = 10
nlist = list(range(n))
print("Printing current and previous number sum in a range(",n,")")
for i in nlist:
    if i == 0:
        j =0
    else:
        j = i-1
    nsum = i + j 
    print("Current Number ",i," Previous Number ",j," Sum: ",nsum)
    
#%%
#   Exercise 3: Print characters from a string that are present at an even index number

def even_index_str(string):
    print("Original String is",string)
    print("Printing only even index chars")
    print("Printing only even index chars")
    for i in range(len(string):
        if i %2 == 0:
            print(string[i])
        
even_index_str("pynative")

#%%
#   Exercise 4: Remove first n characters from a string

def remove_chars(string, n):
    new_string = string[n:]
    print(new_string)
    
remove_chars('hello', 1)

#%%
#   Exercise 5: Check if the first and last number of a list is the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_last_check(nlist):
    first = nlist[0]
    last = nlist[-1]
    result = first == last
    return print("result is",result)

first_last_check(numbers_x)

#%%
#   Exercise 6: Display numbers divisible by 5 from a list

nlist = [10, 22, 33, 46, 55]

def div_by_5(nlist):
    for i in nlist:
        if i%5 ==0:
            print(i)
            
div_by_5(nlist)

#%%
#   Exercise 7: Return the count of a given substring from a string

str_x = "Tomi"
str_y = "Tomi is my bf and he's kinda cool. I like Tomi"

def substring_count(str1, str2):
    list1 = list(str1.split())  
    count = 0
    for word in list1:
        if word == str2:
            count = count +1
    print(str2," appeared ",count, " times")
        
substring_count(str_y, str_x)

#%%

#   Exercise 8: Print the following pattern
for i in range(6):
    stri = str(i) + " "
    print(i*stri)
    
#%%

#   Exercise 9: Check Palindrome Number

def check_palindrome_num(num):
    num_list = list(str(num))
    reversed_list = num_list[::-1]
    print(num_list, reversed_list)
    result = num_list == reversed_list
    if result == True:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palidnrome numer")
        
check_palindrome_num(212)
check_palindrome_num(234)

#%%

#   Exercise 10: Create a new list from a two list using the following condition

def list_generator(list1, list2):
    even_list = [i for i in list2 if i%2 == 0]
    odd_list = [i for i in list1 if i%2 != 0]
    final_list = even_list + odd_list
    print(final_list)
    
l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]
list_generator(l1, l2)

#%%

#    Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

def reversed_digits(num):
    num_list = list(str(num))
    reversed_list = num_list[::-1]
    print(reversed_list)
    
reversed_digits(1234)

#%%

#    Exercise 12: Calculate income tax for the given income by adhering to the below rules

def income_tax(income):
    if income < 10000:
        print("")

#%%

#   Exercise 13: Print multiplication table from 1 to 10

num = 10

for i in range (1, 11):
    for j in range(1, 11):
        mult = i*j
        print(mult, " ")
    print("\t")

#%%

#   Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
l1 = "* * * * * * "
for j in range(1,6):
    l1 = l1[:-2]
    print(l1)

#%%

#   Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base,exp):
    if exp != abs(int(exp)):
        print("Exponent must be non-negative interger")
    elif base != int(base):
        print("Base must be an interger")
    else:
        ans = base**exp
        print(ans)

exponent(10,2)
exponent(-3.4, 3)
exponent(10, 0.2)



