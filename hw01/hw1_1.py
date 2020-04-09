'''
Program: hw1_1.py
Author: Anila Hoxha
Last date modified: 04/2/2020

A sequence 𝑆 contains 𝑛 − 1 unique integers in the range [0, 𝑛 − 1], that is, there is one
number from this range that is not in 𝑆. Design an 𝑂(𝑛) time algorithm for finding that number. You are
only allowed to use 𝑂(1) additional space besides the sequence 𝑆 itself.
'''

def number(S, r, sumS):
    sumR = 0 # Add elements in range # O(1)
    for i in range (r): # O(n)
        sumR += i
    return sumR - sumS # Subtract to find the missing number # O(1)

S = [0, 1, 3, 4, 5, 6] # O(1)
sumS = sum(S) # O(n)
r = len(S) + 1 # Value of range # O(1)
nr = number(S, r, sumS)
print("Missing number in the sequence S: ", nr) # O(1)
