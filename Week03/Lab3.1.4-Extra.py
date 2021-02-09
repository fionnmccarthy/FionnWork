# convert.py
# Lab 3.1  Extra Part
# This program takes in a float amount of dollars and converts it to cent
# Author: Fionn McCarthy

import math

Inputamount = float(input("Please enter an amount:"))
Convertedamount = Inputamount*100
flooredNumber = math.floor(Convertedamount)
print('The amount in cent is:{}'.format(flooredNumber))