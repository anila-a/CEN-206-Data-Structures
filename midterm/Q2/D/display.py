'''
Program: display.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a circularQueue class, using a circularly linked list as storage. Test your class
in testing.py by adding, removing several elements. Submit, circularQueue.py and testing.py.
'''

from circularQueue import *

def display(queue):
    first = queue._tail._next # Start from the head node
    if queue.is_empty(): # Check if the queue is empty
        return 'The queue is empty' # If so, retunr this statement
    while first is not queue._tail: # Not to infinitely display the queue elements, we set this constraint
        print(first._element, '-> ', end = "") # Print the value of the current node
        first = first._next # Go to the next node
    print(first._element, end = "") # And then print the tail node element
