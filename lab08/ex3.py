'''
Program: ex3.py
Author: Anila Hoxha
Last date modified: 05/17/2020

Write a driver code to add N elements
from arr[] to heap, and print out the min heap.
'''

from hpq import *

n = input() # Read user input
n = list(map(int, n.split(" "))) # Convert string to list
p = HeapPriorityQueue() # Create an instance of the class

for i in range(0, len(n)): # Iterate through array elements
    p.add(n[i]) # Add element to heap

print(p.data) # Print min heap
