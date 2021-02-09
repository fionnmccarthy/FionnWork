# floor.py
# Lab 3.1  Part 3
# This program takes in a float and outputs an int rounded down
# Author: Fionn McCarthy

# the math module math.floor() is used here to return the int rounded down
import math
numberTofloor = float(input("Enter a float number:"))
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))
