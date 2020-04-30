'''
Program: p-6.34.py
Author: Anila Hoxha
Last date modified: 04/30/2020

Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.
'''

class ArrayStack():
    # LIFO Stack implementation using a Python list as underlying storage
    def __init__(self): # Create an empty stack
        self._data = []

    def __len__(self): # Return the number of elements in the stack
        return len(self._data)

    def is_empty(self): # Return True if the stack is empty
        return len(self._data) == 0

    def push(self, e): # Add element e to the top of the stack
        self._data.append(e)

    def top(self): # Return (but do not remove) the element at the top of the stack
        if self.is_empty():
            return ('Stack is empty')
        return self._data[-1] # Return the last item in the list

    def pop(self): # Remove and return the element from the top of the stack
        if self.is_empty():
            return ('Stack is empty')
        return self._data.pop()

def postfix(exp):
    s = ArrayStack()

    for i in range(len(exp)):
        if exp[i].isdigit(): # If the character is a digit
            s.push(exp[i]) # Push character into stack
        else: # If the character is an operand
            a = s.pop() # Pop character from stack
            b = s.pop() # Pop character from stack

            s.push(str(eval(b + exp[i] + a)))  # Push the result into stack

    return float(s.pop()) # Return the postfix evaluation

exp = str(input("Enter the expression: ")) # Input the expression
print("Postfix evaluation:", postfix(exp)) # Print the evaluated postfix
