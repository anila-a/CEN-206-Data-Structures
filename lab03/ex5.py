'''
Program: ex5.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a short Python function that takes a positive integer n and returns the sum of the squares
of all the odd positive integers smaller than n.
'''

def sum_of_squares_odd(n):
    sum = 0
    if n % 2 == 0: # If n is even, decrement n by 1, else, do nothing
        n -= 1
    while (n > 0):
        sum += n ** 2 # Add square of the value to sum
        n -= 2 # Decrement n by 2 to pass to the next odd value
    return sum

n = int(input("Enter the value of n: "))
print("Sum of squares is: " + str(sum_of_squares_odd(n)))