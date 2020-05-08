'''
Program: bst.py
Author: Anila Hoxha
Last date modified: 05/08/2020
'''

class BinarySearchTree:

    def __init__(self, value):  # Create the BST
        self.value = value  # Parent node
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):  # Insert new nodes
        if value <= self.value and self.left_child:  # If the element is smaller than the parent node and a left child exists
            self.left_child.insert_node(value)  # Insert for the left child

        elif value <= self.value:  # If the element is smaller than the parent node
            self.left_child = BinarySearchTree(value)  # Insert new node left

        elif value >= self.value and self.right_child:  # If the element is greater than the parent node and a right child exists
            self.right_child.insert_node(value)  # Insert for the right child

        else:  # If the element is greater than the parent node
            self.right_child = BinarySearchTree(value)  # Insert new node right

    def pre_order(self):
        print(self.value, end = " ") # Print the node

        if self.left_child: # Check if there is a left child
            self.left_child.pre_order() # Recursive call

        if self.right_child: # Check if there is a right child
            self.right_child.pre_order() # Recursive call

    def post_order(self):
        if self.left_child: # Check if there is a left child
            self.left_child.post_order() # Recursive call

        if self.right_child: # Check if there is a left child
            self.right_child.post_order() # Recursive call

        print(self.value, end = " ") # Print the node

    def find_min(self):
        if self.value is None: # If there is no root
            return -1
        if self.left_child: # Check if there is a left child
            return self.left_child.find_min() # Recursive call to check further in left children
        else:
            return self.value # Return the minimum value

    def find_max(self):
        if self.value is None: # If there is no root
            return -1
        if self.right_child: # Check if there is a right child
            return self.right_child.find_max() # Recursive call to check further in right children
        else:
            return self.value # Return the maximum value

    def find_node(self, x):
        if self.value is None: # If there is no root
            return False

        if self.value == x: # If the root equals the value we are searching for
            return True

        if self.value < x: # If the node value is less than the value we are searching for
            return self.find_node(self.right_child, x) # Recursive call further to the right

        return self.find_node(self.left_child, x) # Recursive call further to the right
