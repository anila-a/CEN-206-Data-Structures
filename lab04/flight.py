'''
Program: flight.py
Author: Anila Hoxha
Last date modified: 03/21/2020

Design then implement a class to represent a Flight. A Flight has a flight
number, a source, a destination and a number of available seats. The class should have:
• A constructor to initialize the 4 instance variables. You must shorten the name of
the source and the destination by calling the method
shortAndCapital(name).
• Accessor/getters methods for each one of the 4 instance variables.
• Mutator/setters methods for each one of the 4 instance variables except the
flight number instance variable.
• A method reserve(numberOfSeats) to reserve seats on the flight.
(NOTE: You must check that there is enough number of seats to reserve)
• A function cancel(numberOfSeats) to cancel one or more reservations.
• A toString method to easily return the flight information as follows:
A method equal to compare 2 flights.
(NOTE: 2 Flights considered being equal if they have the same flight number,
flg1.equal(flg2))
• A method shortAndCapital(name) to shorten the name of the source and
destination to 3 characters only if it is longer than 3 characters.
'''

class Flight():
    def __init__(self, flightNr, source, destination, seatsNr): # Constructor
        self.flightNr = flightNr
        self.source = source
        self.destination = destination
        self.seatsNr = seatsNr

    # Getter method for flightNr type
    def getFlightNr(self):
        return self.flightNr
    # Getter and Setter methods for source type
    def setSource(self, source):
        self.source = source
    def getSource(self):
        return self.source
    # Getter and Setter methods for destination type
    def setDestination(self, destination):
        self.destination = destination
    def getDestination(self):
        return self.destination
    # Getter and Setter methods for seatsNr type
    def setSeatsNr(self, seatsNr):
        self.seatsNr = seatsNr
    def getSeatsNr(self):
        return self.seatsNr

    # Reserve seats
    def reverse(self, numberOfSeats):
        flag = 0
        if numberOfSeats <= self.seatsNr:
            self.seatsNr = self.seatsNr - numberOfSeats
            flag = 1
        else:
            while flag == 0:
                print("We can't complete your request. There are not enough seats available.")
                numberOfSeats = int(input("Enter another number of seats to reserve: "))
                if numberOfSeats > self.seatsNr:
                    continue
                flag = 1

    # Cancel seats
    def cancel(self, numberOfSeats):
        self.seatsNr = self.seatsNr + numberOfSeats

    # Shorten the name
    def shortAndCapital(self):
        s = self.source[0:3]  # Up to 3rd character
        d = self.destination[0:3]
        print("From: ", s.upper())
        print("To: ", d.upper())

    # Print the flight information
    def toString(self):
        print("Flight No: ", self.flightNr)
        self.shortAndCapital()
    # Compare two flights
    def compare(flg1, flg2):
        if flg1.getFlightNr() == flg2.getFlightNr():
            print("Equal.")
        else:
            print("Not equal.")
