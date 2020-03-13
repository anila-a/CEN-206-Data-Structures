'''
Program: ex9.py
Author: Anila Hoxha
Last date modified: 03/13/2020

Write a pseudo-code description of a function that reverses a list of n integers, so that the
numbers are listed in the opposite order than they were before and compare this method to an
equivalent Python function(reverse()) for doing the same thing.
'''

# Using :, it will not affect the list
# Function reverse_list takes as an argument the list of n integers
# Print list[::-1]

def reverse_list(list):
    print(list[::-1])
    
list = [1, 2, 3]
reverse_list(list)