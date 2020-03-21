'''
Program: mainPolygon.py
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

from polygon import * # Import Polygon class from polygon.py file
# Create objects
poly1 = Polygon()
poly2 = Polygon(8, 5)

print("Polygon 1: ")
print("     # of sides:         ", poly1.getN())
print("     length of a side:   ", poly1.getSide())
print("     Area:                %.2f" %poly1.getArea())
print("     Perimeter:          ", poly1.getPerimeter())

print("Polygon 2: ")
print("     # of sides:         ", poly2.getN())
print("     length of a side:   ", poly2.getSide())
print("     Area:                %.2f" %poly2.getArea())
print("     Perimeter:          ", poly2.getPerimeter())

