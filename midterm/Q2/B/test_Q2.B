'''
Program: test_Q2.B.py
Author: Anila Hoxha
Last date modified: 05/16/2020

Experimentally evaluate the efficiency of the pop method of Pythonâ€™s list class when
using varying indices as a parameter, as we did for insert on Slide 32 - Arrays
(page 205 in your book). Report your results akin to Table 5.5.
'''

from singlyQueue import *
import time

l = SinglyQueue() # Create an instance of the SinglyQueue class

# Enqueue the following values
for i in range(100000000):
    l.enqueue(5)

start_time = time.time() # Start timing
l.dequeue() # Remove the first element from queue
end_time = time.time() # End timing
print(end_time - start_time) # Print duration
