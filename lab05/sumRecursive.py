'''
Program: sumRecursive.py
Author: Anila Hoxha
Last date modified: 04/9/2020

Write a recursive function to get sum of all number from 1 to given
number by user. And draw the recursion trace.
'''

def sumRecursive(n):
    if n == 1: # Base case
        return 1
    return n + sumRecursive(n - 1) # Recursive call

n = int(input("Enter an integer between 1 to 100: "))
print("Sum of numbers from 1 to", n, "is", sumRecursive(n))
