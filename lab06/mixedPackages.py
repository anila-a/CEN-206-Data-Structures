'''
Program: mixedPackages.py
Author: Anila Hoxha
Last date modified: 04/22/2020

When Bob wants to send Alice a message M on the Internet, he breaks M into n data
packets, numbers the packets consecutively, and injects them into the network. When the packets arrive at
Alice’s computer, they may be out of order, so Alice must assemble the sequence of n packets in order
before she can be sure she has the entire message. Describe an efficient scheme for Alice to do this,
assuming that she knows the value of n. What is the running time of this algorithm? (hint: use insertion sort
function to sort packages).
'''

import random

def createList(n):
    s = list(range(n)) # O(1)
    random.shuffle(s) # O(n)
    return s

def sortList(a): # Insertion sort O(n^2)
    for k in range(1, len(a)): # From 1 to n-1
        curr = a[k] # Current element to be inserted
        j = k # Find correct index j for current
        while j > 0 and a[j-1] > curr: # Element list[j-1] must be after current
            a[j] = a[j-1]
            j -= 1
        a[j] = curr # Correct place for curr
    return a

n = int(input("In how many packages do you want to break your message? "))
list = createList(n)
a = [None] * n
for i in list: # O(n)
    a[i] = list[i]
    b = sortList(a)
    print("New Packet: ", list[i], "->  ", sortList(b))
