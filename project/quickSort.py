'''
Program: quickSort.py
Author: Anila Hoxha
Last date modified: 06/26/2020

Implement a non recursive, in-place version of the quick-sort algorithm.
'''

from stack import *

def quickSort(S):
    ''' len() method: O(1) '''
    n = len(S) # Store the number of elements in the list
    if n < 2: # If the number of elements is less than 2
        return S
    ''' For n elements, push operation: O(1) '''
    x = stack([(0, n - 1)]) # Push the list into the stack
    ''' Iteration while condition holds: O(nlogn), dependent on the iteration times '''
    while x: # While the list is in the stack
        ''' Pop operation: O(1) '''
        e, p = low, high = x.pop() # Set e and p equal to low, set high equal to the last element pushed into the stack
        elem = S[e] # Set elem equal to the value of the element in the list stored in index e
        pivot = S[p] # Set pivot equal to the value of the element in the list stored in index p
        ''' Iteration while condition holds: O(nlogn) '''
        while p > e: # Iterate while the value of p is greater than the value of e
            if elem > pivot: # If the value of elem is greater than the pivot
                S[p] = elem # Store elem in the element of the list at index p
                p -= 1 # Change the boundary p of the list: move leftward
                S[e] = elem = S[p] # Set S[e] and the value of elem equal to S[p]
            else: # If the value of elem is less than the pivot
                e += 1 # Change the boundary e of the list: move rightward
                elem = S[e] # Set the value of elem equal to the value of the element in the list at index e
        S[p] = pivot # Set the value of the element in the list at index p equal to pivot

        lsize = p - low # Change the range length of low
        hsize = high - p # Change the range length of high
        if lsize <= hsize: # If the range length of low is less than or equal to the range length of high
            if 1 < lsize:
                ''' Push operations: O(1) '''
                x.push((p + 1, high)) # Push the list in the given range into the stack
                x.push((low, p - 1)) # Push the list in the given range into the stack
        else: # If the range length of low is greater than the range length of high
            ''' Push operation: O(1) '''
            x.push((low, p - 1)) # Push the list in the given range into the stack
        if 1 < hsize:
            ''' Push operation: O(1) '''
            x.push((p + 1, high)) # Push the list in the given range into the stack
    return S # Return the sorted list

''' Total time complexity: O(nlogn) '''