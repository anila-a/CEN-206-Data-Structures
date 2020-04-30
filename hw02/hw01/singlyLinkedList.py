'''
Program: singlyLinkedList.py
Author: Anila Hoxha
Last date modified: 04/28/2020

Experimentally evaluate the efficiency of the pop method of Python’s list class when
using varying indices as a parameter, as we did for insert on Slide 32 - Arrays
(page 205 in your book). Report your results akin to Table 5.5.
'''

class SinglyLinkedList:
    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def _init_(self):
        self.head = self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        temp = self.Node(e, self.head)
        if self.tail == None:
            self.head = self.tail = temp
        self.tail.next = temp
        self.tail = temp
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "The list is empty"
        answer = self.head.element
        self.head = self.head.next
        if(self.head == None):
           self.tail = None
        self.size -= 1
        return answer

    def first(self):
         if self.is_empty():
            return "The list is empty"
         return self.head.element

    def display(self):
        temp = self.head
        if self.is_empty():
            return "The list is empty"
        while (temp != None):
            print(temp.element, '->' , temp = temp.next)