'''
Program: ex5.py
Author: Anila Hoxha
Last date modified: 05/17/2020

How to get max heap results by using the class and its
functions above?
'''

from hpq import *

n = input() # Read user input
n = list(map(int, n.split(" "))) # Convert string to list
p = HeapPriorityQueue() # Create an instance of the class

for i in range(0, len(n)): # Iterate through array elements
    p.add(-1 * n[i]) # Add element to heap, multiply with -1 to get the max heap

for i in range(0, len(n)): # Iterate through array elements
    print(-1 * p.data[i]) # Print min heap, multiply with -1 to print elements as positive
