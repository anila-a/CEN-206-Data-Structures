'''
Program: main.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a singlyQueue class, using a singly linked list as storage. Test your class in testing.py
by adding, removing several elements. Submit, singlyQueue.py and testing.py.
'''

from display import *

l = SinglyQueue() # Create an instance of the SinglyQueue class

# Enqueue the following values
l.enqueue(11)
l.enqueue(23)
l.enqueue(36)
l.enqueue(47)

print(l.first()) # Display the first element in the queue

display(l) # Display the whole queue

l.dequeue() # Remove the first element from queue

print() # New line
display(l) # Display the whole queue
