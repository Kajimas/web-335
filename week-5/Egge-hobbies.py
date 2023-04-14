"""
Title: Egge_hobbies.py
Written by: William Egge
Description: A python document that serves as "Hello World" for this assignment 
Date: 2023-03-25

This module contains several functions that perform various tasks.

"""

# my list of 5 hobbies
hobbies = ["reading", "drawing", "gaming", "exercise", "cooking"]

# a for loop that prints each hobby in the list
for hobby in hobbies:
    print(hobby)

# a list of the days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# a for loop that starts by printing my hobbies to the console
# the loop then prints the days of the week and a message
# if the day is Saturday or Sunday, the message is "You are off! Enjoy your hobbies."
# if the day is not Saturday or Sunday, the message is "It's a work day."
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"{day} - You are off! Enjoy your hobbies.")
    else:
        print(f"{day} - It's a work day.")
