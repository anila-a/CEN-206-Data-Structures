'''
Program: sumSeries.py
Author: Anila Hoxha
Last date modified: 04/9/2020

Write a recursive function to compute the following series:
m(i) = 1 + 1/2 + 1/3 + ⋯ + 1/i

Write a test program that displays m(i) for i = 1, 2, 3, ... , 10.
'''

def sumSeries(i):
    if i == 1: # Base case
        return 1
    return (1 / i) + sumSeries(i - 1) # Direct recursion

def printSeries(i):
    for n in range(i, 11):
        print("For i =", i, " the sum is: %.2f" %sumSeries(i)) # Indirect recursion
        i += 1

i = 1
printSeries(i)
