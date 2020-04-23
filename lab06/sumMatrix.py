'''
Program: sumMatrix.py
Author: Anila Hoxha
Last date modified: 04/20/2020

Use standard control structures to compute the sum of all numbers in an 𝑛 × 𝑛 data
set, represented as a list of lists.
'''

m = [[1, 2, 3], [4, 5, 6]] # Initialize the matrix
sum = 0
for i in range(2):
    for j in range(3):
        sum += m[i][j] # Add elements to sum
print(sum)
