'''
Program: testing.py
Author: Anila Hoxha
Last date modified: 04/28/2020

Write a singlyQueue class, using a singly linked list as storage. Test your class in testing.py
by adding, removing several elements. Submit, singlyQueue.py and testing.py.
'''

from singlyQueue import *

def display(queue):
    first = queue._head
    if queue.is_empty():
        return 'The queue is empty'
    while first is not None:
        print(first._element, '-> ', end = "")
        first = first._next

l = SinglyQueue()
# Enqueue elements in the queue
l.enqueue(1)
l.enqueue(2)
l.enqueue(3)
l.enqueue(4)
print(l.first()) # Display first element
display(l) # Display queue
l.dequeue() # Remove element from queue
print() # New line
display(l) # Display queue
