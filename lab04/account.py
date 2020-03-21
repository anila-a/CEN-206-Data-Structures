'''
Program: account.py
Author: Anila Hoxha
Last date modified: 03/21/2020

Design a class named Account for clients in a bank. The class contains:
• A constructor with the instance variables name, pin, and balance.
• Three getter methods for the instance variables.
• A deposit method that adds specified amount of money to the balance
• A withdraw method that withdraw the money from the balance.
i. If not enough money return ‘Insufficient funds’
• A report method that reports name, pin and balance of the client.
'''

class Account():
    def __init__(self, name, pin, balance): # Constructor
        self.name = name
        self.pin = pin
        self.balance = balance
    # Getter methods for each type
    def getName(self, name):
        self.name = name
    def getPin(self, pin):
        return self.pin
    def getBalance(self, balance):
        return self.balance
    # Add specified amount of money to balance
    def deposit(self, other):
        self.balance = self.balance + other
    # Subtract specified amount of money from balance
    def withdraw(self, other):
        if other > self.balance:
            print("Insufficent funds.")
        else:
            self.balance = self.balance - other
    def report(self, name, pin):
        print("Name: ", self.name, ", Pin: ", self.pin, ", Balance: ", self.balance)