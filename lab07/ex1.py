'''
Program: ex1.py
Author: Anila Hoxha
Last date modified: 05/08/2020

Given a Binary Search Tree class. Write an insert_node(value) function which insert the nodes in their
proper places in BST.
'''

from bst import *

n = input()
n = list(map(int, n.split(" "))) # Split the string
tree = BinarySearchTree(n[0]) # Create root
for i in range(1, len(n)): # Iterate through node values
    tree.insert_node(n[i]) # Create child nodes

