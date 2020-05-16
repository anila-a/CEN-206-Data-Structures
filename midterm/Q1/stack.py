'''
Program: stack.py
Author: Anila Hoxha
Last date modified: 05/14/2020

Implement a program that can input an expression in postfix notation (see
Exercise C-6.22) and output its value.
'''

class ArrayStack():
    # LIFO Stack implementation using a Python list as underlying storage
    def __init__(self): # Constructor
        self._data = [] # Create an empty stack

    def __len__(self): # Find the length of the stack
        return len(self._data) # Return the number of elements in the stack

    def is_empty(self): # Check if the stack is empty or not
        return len(self._data) == 0 # Return True if the stack is empty

    def push(self, e):
        self._data.append(e) # Add element e to the top of the stack

    def top(self): # Return (but do not remove) the element at the top of the stack
        if self.is_empty(): # Check if the stack is empty or not
            return ('Stack is empty') # If so, return this statement
        return self._data[-1] # If not, return the last item in the list

    def pop(self): # Remove and return the element from the top of the stack
        if self.is_empty(): # Check if the stack is empty or not
            return ('Stack is empty') # If so, return this statement
        return self._data.pop() # If not, remove and return the last item in the list
