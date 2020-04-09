'''
Program: hw1_3.py
Author: Anila Hoxha
Last date modified: 04/2/2020

A sequence 𝑆 contains 𝑛 integers taken from the interval [0, 4𝑛], with repetitions allowed.
Describe an efficient algorithm for determining an integer value 𝑘 that occurs the most often in 𝑆. What
is the running time of your algorithm?
'''

def occurrence(s):
    occ = {}
    k = 0 # O(1)
    for i in s: # O(n)
        if i in occ: # O(n)
            occ[i] += 1
        else:
            occ[i] = 1 # New occurrence
        if occ[i] > k: # Compare to the value stored in max # O(n)
            k = i # Store the number which occurs more often
    return k # O(1)

n = 10
s = [1, 2, 8, 11, 12, 12, 12, 34, 37, 38]
l = len(s)
print(occurrence(s)) # Print k
