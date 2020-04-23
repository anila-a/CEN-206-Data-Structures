'''
Program: sumMatrix2.py
Author: Anila Hoxha
Last date modified: 04/20/2020

Describe how the built-in sum function can be combined with Python’s comprehension
syntax to compute the sum of all numbers in an 𝑛 × 𝑛 data set, represented as a list of lists.
'''

import numpy as np
m = [[1, 2, 3], [4, 5, 6]] # Initialize the matrix
print(np.sum(m))