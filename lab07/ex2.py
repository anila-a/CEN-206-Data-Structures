'''
Program: ex2.py
Author: Anila Hoxha
Last date modified: 05/08/2020

Given an array arr[] of N nodes representing preorder traversal of BST. The task is to print its
preorder/postorder traversal.
'''

from bst import *

n = input()
n = list(map(int, n.split(" "))) # Split the string
tree = BinarySearchTree(n[0]) # Create root
for i in range(1, len(n)): # Iterate through node values
    tree.insert_node(n[i]) # Create child nodes

print("Pre-order traversal:")
tree.pre_order() # Print the nodes in pre-order

print("\n\nPost-order traversal:")
tree.post_order() # Print the nodes in post-order