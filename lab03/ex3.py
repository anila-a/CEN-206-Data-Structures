'''
Program: ex3.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the
built-in functions min or max in implementing your solution.
'''

def minmax(data):
    min = 999
    max = -999
    for i in range(n):
        if data[i] < min:
            min = data[i] # Assign the new value to min
    for i in range(n):
        if data[i] > max:
            max = data[i] # Assign the new value to max
    return min, max

data = []
n = int(input("How many numbers in the sequence? "))
for i in range(n):
    num = int(input("Enter a number: "))
    data.append(num) # Add input to data
print(minmax(data)) # Call the function and print the tuple