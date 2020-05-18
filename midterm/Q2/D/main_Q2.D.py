'''
Program: main_Q2.D.py
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

l = CircularQueue() # Create an instance of the CircularQueue class
# Enqueue elements in the queue
l.enqueue(21)
l.enqueue(38)
l.enqueue(55)
l.enqueue(79)

display(l) # Display the whole queue

l.dequeue() # Remove the first element from queue

print() # New line
display(l) # Display the whole queue

print() # New line
l.rotate() # Rotate front element to the back of the queue
display(l) # Display the whole queue