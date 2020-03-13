'''
Program: ex16.py
Author: Anila Hoxha
Last date modified: 03/11/2020

Write a Python program that can take a positive integer greater than 2 as input and write out the
number of times one must repeatedly divide this number by 2 before getting a value less than 2.
'''

def division(i):
    cnt = 0
    while i >= 2:
        i /= 2
        if i >= 2: # Check if still greater than or equal to 2
            cnt += 1
    return cnt

i = int(input("Enter an integer greater than 2: "))
while i < 2: # If input is not greater than 2
    i = int(input("Enter an integer greater than 2: "))
print(division(i))