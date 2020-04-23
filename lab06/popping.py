'''
Program: popping.py
Author: Anila Hoxha
Last date modified: 04/20/2020

Modify the experiment from Code Fragment 5.1(Slide 25) in order to demonstrate that
Python’s list class occasionally shrinks the size of its underlying array when
elements are popped from a list.
'''

import sys # Provides getsizeof function
data = []
print('Appending the list: ')
for k in range(13):
    a = len(data) # Number of elements
    b = sys.getsizeof(data) # Actual size in bytes
    print('Length: {0:2d}; Size in bytes: {1:3d}'.format(a,b)) # Increase length by one
    data.append(None)

print('\nPopping elements from the list: ')
for i in range(12, -1, -1):
    c = len(data) # Number of elements
    d = sys.getsizeof(data) # Actual size in bytes
    print('Length: {0:2d}; Size in bytes: {1:3d}'.format(c,d)) # Increase length by one
    data.pop()