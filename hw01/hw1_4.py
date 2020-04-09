'''
Program: hw1_4.py
Author: Anila Hoxha
Last date modified: 04/2/2020

Perform an experimental analysis of the three algorithms prefix_average1, prefix_average2,
and prefix_average3, from Slides. Compare them with 100, 1000, 10000, and 100000 input sizes.
'''

import time

def prefix_average1(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total/(j+1)
    return A

def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1])/(j+1)
    return A

def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0
    for j in range(n):
        total += S[j]
        A[j] = total/(j+1)
    return A

'''print("For prefix_average1: ")
# 100
start_time = time.time()
prefix_average1([3] * 100)
end_time = time.time()
duration = end_time - start_time
print("For 100 input size ", duration)
# 1000
start_time = time.time()
prefix_average1([3] * 1000)
end_time = time.time()
duration = end_time - start_time
print("For 1000 input size ", duration)
# 10000
start_time = time.time()
prefix_average1([3] * 10000)
end_time = time.time()
duration = end_time - start_time
print("For 10000 input size ", duration)
# 100000
#start_time = time.time()
#prefix_average1([3] * 100000)
#end_time = time.time()
#duration = end_time - start_time
#print("For 100000 input size ", duration)'''

'''print("For prefix_average2: ")
# 100
start_time = time.time()
prefix_average2([3] * 100)
end_time = time.time()
duration = end_time - start_time
print("For 100 input size ", duration)
# 1000
start_time = time.time()
prefix_average2([3] * 1000)
end_time = time.time()
duration = end_time - start_time
print("For 1000 input size ", duration)
# 10000
start_time = time.time()
prefix_average2([3] * 10000)
end_time = time.time()
duration = end_time - start_time
print("For 10000 input size ", duration)
# 100000
start_time = time.time()
prefix_average2([3] * 100000)
end_time = time.time()
duration = end_time - start_time
print("For 100000 input size ", duration)'''

print("For prefix_average3: ")
# 100
start_time = time.time()
prefix_average3([3] * 100)
end_time = time.time()
duration = end_time - start_time
print("For 100 input size ", duration)
# 1000
start_time = time.time()
prefix_average3([3] * 1000)
end_time = time.time()
duration = end_time - start_time
print("For 1000 input size ", duration)
# 10000
start_time = time.time()
prefix_average3([3] * 10000)
end_time = time.time()
duration = end_time - start_time
print("For 10000 input size ", duration)
# 100000
start_time = time.time()
prefix_average3([3] * 100000)
end_time = time.time()
duration = end_time - start_time
print("For 100000 input size ", duration)