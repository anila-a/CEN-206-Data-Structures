'''
Program: circularQueue.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a circularQueue class, using a circularly linked list as storage. Test your class
in testing.py by adding, removing several elements. Submit, circularQueue.py and testing.py.
'''

class CircularQueue:
    # Queue implementation using circularly linked list for storage
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next): # Constructor
            self._element = element # Value of the node
            self._next = next # Reference to the next node

    def __init__(self): # Constructor
    # Create an empty queue
        self._tail = None # No initial value
        self._size = 0

    def __len__(self): # Find the length of the queue
        return self._size # Return the number of elements in the queue

    def is_empty(self): # Check if the queue is empty or not
        return self._size == 0 # Return True if the queue is empty

    def first(self):
    # Return (but do not remove) the element at the front of the queue
        if self.is_empty(): # If the queue is empty
            return ('Queue is empty') # If so, return this statement
        head = self._tail._next # Head of the queue
        return head._element # Return the value of head

    def dequeue(self):
    # Remove and return the first elements of the queue
        if self.is_empty(): # If the queue is empty
            return ('Queue is empty') # If so, return this statement
        oldhead = self._tail._next
        if self._size == 1: # Removing only element
            self._tail = None
        else:
            self._tail._next = oldhead._next # Bypass the old head
        self._size -= 1 # Decrement size by 1
        return oldhead._element

    def enqueue(self, e):
    # Add an element to the back of the queue
        newest = self._Node(e, None) # Node will be new tail node
        if self.is_empty(): # If the queue is empty
            newest._next = newest # Initialize circularly
        else: # If not
            newest._next = self._tail._next # New node points to head
            self._tail._next = newest # Old tail points to new node
        self._tail = newest # New node becomes the tail
        self._size += 1 # Increment the queue size by one

    def rotate(self):
    # Rotate front element to the back of the queue
        if self._size > 0: # If there are elements in the queue
            self._tail = self._tail._next # Old head becomes new tail
