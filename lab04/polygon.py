'''
Program: polygon.py
Author: Anila Hoxha
Last date modified: 03/21/2020

Design a class named Polygon to represent a regular polygon. In regular
polygon, all the sides have the same length. The class contains:

Constructor: Instance Variable: n – number of sides with default value 3,
side – length of the side with default value 1.

Methods:
• Getters and Setters methods for all instance variables
• getPerimeter() that returns the perimeter of the polygon.
• getArea() that returns the area of the polygon.

Use the following test program mainPolygon.py that creates two Polygon objects - one
with no-arg constructor and the other with Polygon(8, 5).
'''

import math

class Polygon():
    def __init__(self, n = 3, side = 1): # Constructor
        self.n = n
        self.side = side

    # Getter and Setter methods for n type
    def setN(self, n):
        self.n = n
    def getN(self):
        return self.n

    # Getter and Setter methods for side type
    def setSide(self, side):
        self.side = side
    def getSide(self):
        return self.side

    def getArea(self): # Return area of polygon
        return (self.n * (self.side ** 2)) / (4 * math.tan(math.pi / self.n))

    def getPerimeter(self): # Return perimeter of polygon
        return self.side * self.n