'''
Program: ex4.py
Author: Anila Hoxha
Last date modified: 05/08/2020

Given a Binary Search Tree. The task is to find the maximum element in this given BST. If the tree is empty,
there is no minimum element, so print -1 in that case.
'''

from bst import *

n = input()
n = list(map(int, n.split(" "))) # Split the string
tree = BinarySearchTree(n[0]) # Create root
for i in range(1, len(n)): # Iterate through node values
    tree.insert_node(n[i]) # Create child nodes

print(tree.find_max()) # Print the node with the maximum value