'''
Program: ex1.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a short Python function, is_multiple(n, m), that takes two integer values and returns True
if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
'''

def is_multiple(n, m):
    if n % m == 0: # Check if remainder is zero
        return 1
    else:
        return 0

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
if is_multiple(n, m) == 1: # If return value is true
    print("True")
else:
    print("False")
