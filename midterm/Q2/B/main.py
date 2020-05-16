'''
Program: main.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a circularQueue class, using a circularly linked list as storage. Test your class
in testing.py by adding, removing several elements. Submit, circularQueue.py and testing.py.
'''

from display import *

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
