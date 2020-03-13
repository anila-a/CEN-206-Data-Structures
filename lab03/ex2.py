'''
Program: ex2.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a short Python function, is_even(k), that takes an integer value and returns True if k is
even, and False otherwise. However, your function cannot use the multiplication, modulo, or
division operators.
'''

def is_even(k):
    return (k & 1) # Using bitwise operator

k = int(input("Enter the value of k: "))
if is_even(k) == 0:
    print("Even")
else:
    print("Odd")