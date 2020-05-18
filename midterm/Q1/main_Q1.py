'''
Program: main_Q1.py
Author: Anila Hoxha
Last date modified: 05/14/2020

Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.
'''

from postfix import *

''' Test the program with sample input: 52+83-*4/ '''

exp = str(input("Enter the expression: ")) # Read the user input
print("Postfix evaluation:", postfix(exp)) # Print the postfix evaluation of the expression
