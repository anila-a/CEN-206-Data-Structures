'''
Program: appending.py
Author: Anila Hoxha
Last date modified: 04/20/2020

Execute the experiment from Code Fragment 5.1 (Slide 25) and compare the results
on your system to those it is reported in Slide 25.
'''

import sys # Provides getsizeof function
data = []
for k in range(13):
    a = len(data) # Number of elements
    b = sys.getsizeof(data) # Actual size in bytes
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b)) # Increase length by one
    data.append(None)
