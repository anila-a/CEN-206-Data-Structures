'''
Program: hpq.py
Author: Anila Hoxha
Last date modified: 05/17/2020

Heap Priority Queue class.
'''

import math

class HeapPriorityQueue:

    def __init__(self):
        # Create a new empty priority queue
        self.data = []

    def __len__(self):
        # Return the number of items in the priority queue
        return len(self.data)

    def parent(self, j):
        # Return the parent of j node
        return (j - 1) // 2

    def left(self, j):
        # Return the left child of j node
        return 2 * j + 1

    def right(self, j):
        # Return the right child of j node
        return 2 * j + 2

    def hasLeft(self, j):
        # Return True if element at indices j has a left child
        return self.left(j) < len(self.data)

    def hasRight(self, j):
        # Return True if element at indices j has a right child
        return self.right(j) < len(self.data)

    def swap(self, i, j):
        # Swap elements at indices i and j
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def upheap(self, j):
        # Compare the element and indices j with its parent and swap if the parent is larger
        parent = self.parent(j) # Find parent
        if j > 0 and self.data[j] < self.data[parent]: # If element in j is smaller than element in parent
            self.swap(j, parent) # Swap values
            self.upheap(parent) # Recursive call

    def downheap(self, j):
        # Compare the element at indices j with its left and right children, then swap the parent with the smaller child
        if self.hasLeft(j): # If there exists a left child
            left = self.left(j) # Find the left child
            small = left # Assign left to small
            if self.hasRight(j): # If there exists a right child
                right = self.right(j) # Find the right child
                if self.data[right] < self.data[left]: # If right child is smaller than left child
                    small = right # Assign right to small
                if self.data[small] < self.data[j]: # If small child is smaller than the element in j
                    self.swap(j, small) # Swap values
                    self.downheap(small) # Recursive call

    def add(self, value):
        # Add a value at the end of the priority queue
        # Fix the heap
        self.data.append(value) # Append value
        self.upheap(len(self.data) - 1) # Fix the heap

    def min(self):
        # Return (do not remove) the minimum value from the queue
        if self.data is None: # If the priority queue is empty
            return ("Priority queue is empty.") # Return this statement
        min = self.data[0] # Since this is a min-heap, the root is the smallest element
        # return (item.key, item.value)
        return min

    def removeMin(self):
        # Return and remove the minimum value from the priority queue
        # Fix the heap
        if self.data is None: # If the priority queue is empty
            return ("Priority queue is empty.") # Return this statement
        self.swap(0, len(self.data) - 1) # Swap the root with the last node of the heap
        min = self.data.pop() # Remove the previous root node
        self.downheap(0) # Fix the heap
        return min

    def heightHeap(self):
        # Calculate the height of the heap of size N
        return math.ceil(math.log(len(self.data))) # Return the height of heap

    def k_smallestElement(self, k):
        # Return k smallest element from the array
        # Output should be printed in increasing order
        for i in range(k): # Iterate through values until k
            print(self.removeMin(), end = " ") # Print and call recursively
        '''
        How to call this method in main?
        
        p = HeapPriorityQueue()
        for i in range(0, len(n)):
            p.add(n[i])
        p.k_smallestElement(3)
        '''

    def k_largestElement(self, k):
        # Return k largest element from the array
        # Output should be printed in decreasing order
        self.data.sort(reverse = False) # Sort data in heap
        for i in range(k):  # Iterate through values until k
            print(self.data[i] * -1, end = " ") # Print and call recursively
        '''
        How to call this method in main?
        
        p = HeapPriorityQueue()
        for i in range(0, len(n)):
            p.add(-1*n[i])
        p.k_largestElement(3)
        '''
