'''
Program: main.py
Author: Anila Hoxha
Last date modified: 06/26/2020

Implement a non recursive, in-place version of the quick-sort algorithm.
'''

from quickSort import *
import time

# S = [7, 5, 11, 3, 2, 6] # Non-sorted list
# quickSort(S) # Call the function to sort the list
# print(S) # Print the sorted list

S = [1] * 100000
start_time = time.time()
quickSort(S)
end_time = time.time()
print(end_time - start_time)
