'''
Program: ex14.py
Author: Anila Hoxha
Last date modified: 03/13/2020

Write a short Python program that takes two arrays a and b of length n storing int values, and
returns the dot product of a and b. That is, it returns an array c of length n such that c[i] =
a[i] · b[i], for i = 0, . . . ,n−1.
'''

def dot_product(a, b, n):
    c = []
    for i in range(0, n, 1):
        c.append(a[i] * b[i]) # Add product to c
    return c

a = []
b = []
n = int(input("Enter the value of n: "))
print("Enter the first array: ")
for i in range(n):
    a.append(int(input())) # Add elements in the array
print("Enter the second array: ")
for i in range(n):
    b.append(int(input())) # Add elements in the array
print(dot_product(a, b, n)) # Call the function to print the dot product