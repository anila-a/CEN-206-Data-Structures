'''
Program: mainFlight.py
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

from flight import * # Import Flight class from flight.py file
# Create objects
flg1 = Flight(flightNr = 5432, source = "Tirana", destination = "Vienna", seatsNr = 100)
flg2 = Flight(flightNr = 2345, source = "Vienna", destination = "Munich", seatsNr = 100)
# Reserve
nrR = int(input("Enter the number of seats you want to reserve: "))
flg1.reverse(nrR)
# Cancel
nrC = int(input("Enter the number of seats you want to cancel: "))
flg1.cancel(nrC)
# Print flight information
print("Your flight information: ")
flg1.toString()
# Compare two flights
Flight.compare(flg1, flg2)
