'''
Name: emailParser.py
Author: Anila Hoxha
Created: 03/03/2020
Description: Write a program that prompts user for her/his email address in this
format: “firstname.lastname@epoka.edu.al”. The application parses the email to first
name, last name and host name.
'''

email = str(input("Enter your email address (firstname.lastname@epoka.edu.al): "))
sep1 = email.find(".") # Store the position
sep2 = email.find("@") # Store the position
print("First Name: " + email[0:sep1])
print("Last Name: " + email[sep1+1:sep2])
print("Host Name: " + email[sep2+1:len(email)])