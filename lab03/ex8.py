'''
Program: ex8.py
Author: Anila Hoxha
Last date modified: 03/10/2020

Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16,
32, 64, 128, 256].
'''

a = [2 ** n for n in range(9)]
print(a)