'''
Program: ex4.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a short Python function that takes a positive integer n and returns the sum of the squares
of all the positive integers smaller than n.
'''

def sum_of_squares(n):
    sum = 0
    while (n > 0):
        sum += n ** 2 # Add square of the value to sum
        n -= 1
    return sum

n = int(input("Enter the value of n: "))
print("Sum of squares is: " + str(sum_of_squares(n)))