'''
Program: ex4.py
Author: Anila Hoxha
Last date modified: 05/17/2020

Remove all the elements from the heap
by using removeMin() function.
'''

from hpq import *

n = input() # Read user input
n = list(map(int, n.split(" "))) # Convert string to list
p = HeapPriorityQueue() # Create an instance of the class

for i in range(0, len(n)): # Iterate through array elements
    p.add(n[i]) # Add element to heap

for i in range(0, len(n)): # Iterate through array elements
    print(p.removeMin(), end = " ") # Print elements
