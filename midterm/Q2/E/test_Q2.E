'''
Program: test_Q2.E.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Compare the results of classic Queue, singlyQueue, and circularQueue for pop(0) method.
Explain the results with your words.
'''

from singlyQueue import *
from circularQueue import *
import time

'''
l = SinglyQueue() # Create an instance of the SinglyQueue class

# Enqueue the following values
for i in range(100000000):
    l.enqueue(5)

start_time = time.time() # Start timing
l.dequeue() # Remove the first element from queue
end_time = time.time() # End timing
print(end_time - start_time) # Print duration
'''

queue = []

# Enqueue the following values
for i in range(1000000000):
    queue.append(5)

start_time = time.time() # Start timing
queue.pop(0) # Remove the first element from queue
end_time = time.time() # End timing
print(end_time - start_time) # Print duration

'''
l = CircularQueue() # Create an instance of the SinglyQueue class

# Enqueue the following values
for i in range(1000000000):
    l.enqueue(5)

start_time = time.time() # Start timing
l.dequeue() # Remove the first element from queue
end_time = time.time() # End timing
print(end_time - start_time) # Print duration
'''
