'''
Program: postfix.py
Author: Anila Hoxha
Last date modified: 05/14/2020

Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.
'''

from stack import *

def postfix(exp):
    s = ArrayStack() # Create an instance of the ArrayStack class

    for i in range(len(exp)): # Check the expression characters one by one
        if exp[i].isdigit(): # If the character is a digit
            s.push(exp[i]) # Push character into stack
        else: # If the character is an operand
            a = s.pop() # Pop character from stack
            b = s.pop() # Pop character from stack
            # Use built-in function eval to parse the argument and evaluate it as an expression
            s.push(str(eval(b + exp[i] + a)))  # Push the result into stack
    # There might be evaluations which result in decimal numbers
    # For this reason, return a float value
    return float(s.pop()) # Return the postfix evaluation
