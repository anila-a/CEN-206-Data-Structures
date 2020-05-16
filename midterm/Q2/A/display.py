'''
Program: display.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a singlyQueue class, using a singly linked list as storage. Test your class in testing.py
by adding, removing several elements. Submit, singlyQueue.py and testing.py.
'''

from singlyQueue import *

def display(queue):
    first = queue._head # Start from the head node
    if queue.is_empty(): # Check if the queue is empty
        return 'The queue is empty' # If so, return this statement
    while first is not None: # If not, for each element in the queue, print its value
        print(first._element, '-> ', end = "") # Print the value of the current node
        first = first._next # Go to the next node
    print(end = "None") # At the end, print None
