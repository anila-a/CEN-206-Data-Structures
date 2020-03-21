'''
Program: mainQuadratic.py
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

from quadratic import * # Import Quadratic class from quadratic.py file

print("Enter the coefficients a b c (separate them with a space): ")
list = input()
a, b, c = list.split()

# Create objects
q = Quadratic(int(a), int(b), int(c))
if q.getDiscriminant() > 0:
   print("There are two roots: Root 1: %.2f" %q.getRoot1(), " Root 2: %" %q.getRoot2())
elif q.getDiscriminant() == 0:
    print("There is one root: %.2f" %q.getRoot1())
else:
    print("The equation has no roots.")







