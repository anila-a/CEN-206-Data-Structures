'''
Program: experimentPop.py
Author: Anila Hoxha
Last date modified: 04/20/2020

Experimentally evaluate the efficiency of the pop method of Python’s list class when
using varying indices as a parameter, as we did for insert on Slide 32
(page 205 in your book). Report your results as in Table 5.5.
'''

import time

data = [0] * 1000000
n1 = 0
n2 = len(data)
n3 = n2 / 2
# Case 1
start_time = time.time()
for i in range(n1):
    data.pop(n1)
end_time = time.time()
print("For k = 0, the running time is: ", end_time - start_time)
# Case 2
start_time = time.time()
for i in range(int(n3)):
    data.pop(int(n3))
end_time = time.time()
print("For k = n/2, the running time is: ", end_time - start_time)
# Case 3
start_time = time.time()
for i in range(n2):
    data.pop()
end_time = time.time()
print("For k = n, the running time is: ", end_time - start_time)