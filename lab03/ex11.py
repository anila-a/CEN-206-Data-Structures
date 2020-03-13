'''
Program: ex11.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a Python function that takes a sequence of numbers and determines if all the numbers are
different from each other (that is, they are distinct).
'''

def distinct(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

list = [2, 2, 33, 46, 52, 18]
print(distinct(list))