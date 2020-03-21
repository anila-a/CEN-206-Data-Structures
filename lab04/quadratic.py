'''
Program: quadratic.py
Author: Anila Hoxha
Last date modified: 03/21/2020

Design a class named Quadratic for a quadratic equation: ax2 + bx + cx = 0.
The class contains:
• A constructor with the instance variables a, b, and c that represent three
coefficients.
• Three getter methods for a, b, and c.
• A method getDiscriminant() that returns the discriminant, which is b2-4ac.
• The methods named getRoot1() and getRoot2() for returning two
roots of the equation.

Write a test program mainQuadratic.py that prompts the user to enter values for a,
b, and c and displays the result based on the discriminant.
If the discriminant positive, display two roots.
If the discriminant is 0, display the one root.
If the discriminant is less than 0, display “The equation has no roots”.
'''

import math

class Quadratic():
    def __init__(self, a, b, c): # Constructor
        self.a = a
        self.b = b
        self.c = c
    # Getter methods for a, b, c
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    # Getter for discriminant
    def getDiscriminant(self):
        return math.pow(self.b, 2) - 4 * self.a * self.b
    # Getter for roots
    def getRoot1(self):
        return (-self.b) + math.sqrt(self.getDiscriminant())
    def getRoot2(self):
        return (-self.b) - math.sqrt(self.getDiscriminant())



