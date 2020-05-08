'''
Program: ex5.py
Author: Anila Hoxha
Last date modified: 05/08/2020

Given a Binary Search Tree (BST) in question 3, you need to find if a particular node(data) is present in
the BST or not. If present print 1, else print 0.
'''

from bst import *

n = input()
n = list(map(int, n.split(" "))) # Split the string
tree = BinarySearchTree(n[0]) # Create root
for i in range(1, len(n)): # Iterate through node values
    tree.insert_node(n[i]) # Create child nodes

if tree.find_node(32): # Call the function to find if the node is in bst
    print("Node found!")
else:
    print("Node not found!")
