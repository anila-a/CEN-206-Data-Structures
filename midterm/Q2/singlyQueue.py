'''
Program: singlyQueue.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Write a singlyQueue class, using a singly linked list as storage. Test your class in testing.py
by adding, removing several elements. Submit, singlyQueue.py and testing.py.
'''

class SinglyQueue:
    # FIFO queue implementation using a singly linked list for storage
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, next): # Constructor
            self._element = element # Value of the node
            self._next = next # Reference to the next node

    def __init__(self): # Constructor
    # Create an empty queue
        self._head = None # No initial value
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
        return self._head._element # If not, return the first element in the queue

    def dequeue(self):
    # Remove and return the first element of the queue
        if self.is_empty(): # If the queue is empty
            return ('Queue is empty') # If so, return this statement
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1 # Decrement size by 1
        if self.is_empty(): # Special case as queue is empty
            self._tail = None # Removed head had been the tail
        return ans

    def enqueue(self, e):
    # Add an element to the back of queue
        newest = self._Node(e, None) # Node will be new tail node
        if self.is_empty(): # If the queue is empty
            self._head = newest # Special case: previously empty
        else:
            self._tail._next = newest # Tail node references to the newest node
        self._tail = newest # Update reference to tail node
        self._size += 1 # Increment size with one
