'''
Program: circularQueue.py
Author: Anila Hoxha
Last date modified: 04/28/2020

Write a circularQueue class, using a circularly linked list as storage. Test your class
in testing.py by adding, removing several elements. Submit, circularQueue.py and testing.py.
'''

from circularQueue import *

def display(queue):
    first = queue._head
    if queue.is_empty():
        return 'The queue is empty'
    while True:
        print(first._element, '-> ', end = "")
        first = first._next

l = CircularQueue()
# Enqueue elements in the queue
l.enqueue(1)
l.enqueue(2)
l.enqueue(3)
l.enqueue(4)
display(l) # Display queue
l.dequeue() # Remove element from queue
print() # New line
display(l) # Display queue
