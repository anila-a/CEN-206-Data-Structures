'''
Program: testing2.py
Author: Anila Hoxha
Last date modified: 04/28/2020

Experimentally evaluate the efficiency of the pop method of Python’s list class when
using varying indices as a parameter, as we did for insert on Slide 32 - Arrays
(page 205 in your book). Report your results akin to Table 5.5.
'''
import time
from singlyLinkedList import *

l = SinglyLinkedList()
l.push([0] * 1000)

start_time = time.time()
l.pop(0)
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
l.pop(-1)
end_time = time.time()
print(end_time - start_time)

