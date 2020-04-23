'''
Program: repeated.py
Author: Anila Hoxha
Last date modified: 04/22/2020

Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive, with exactly one
repeated. Describe a fast algorithm for finding the integer in A that is repeated.
'''

def repeated(list):
    sortList(list) # Sort the elements in the list
    i = None # Set a temporary variable to None
    for k in list: # Iterate through the sorted elements
        if k == i: # If condition is met
            return i # Return the repeated value
        i = k # Else, assign the value to i

def sortList(list): # Insertion sort
    for k in range(1, len(list)): # From 1 to n-1
        curr = list[k] # Current element to be inserted
        j = k # Find correct index j for current
        while j > 0 and list[j-1] > curr: # Element list[j-1] must be after current
            list[j] = list[j-1]
            j -= 1
        list[j] = curr # Correct place for curr
    return list

list = [1, 5, 2, 5, 7, 3, 9, 13, 15]
print(repeated(list))