'''
Program: flowers.py
Author: Anila Hoxha
Last date modified: 03/21/2020

Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals,
and its price. Your class must include a constructor method that initializes each variable
to an appropriate value, and your class should include methods for setting the value of
each type and retrieving the value of each type.
'''

class Flower:
    def __init__(self, name, petals, price): # Constructor
        self.name = name
        self.petals = petals
        self.price = price

    # Getter and Setter methods for name type
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    # Getter and Setter methods for petals type
    def setPetals(self, petals):
        self.petals = petals
    def getPetals(self):
        return self.petals

    # Getter and Setter methods for price type
    def setPrice(self, price):
        self.price = price
    def getPrice(self):
        return self.price
