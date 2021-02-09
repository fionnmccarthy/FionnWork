# absolute.py
# Lab 3.1  Part 2
# This program takes in number and give its absolutevalue (ie -4 or 4 would both output 4)
# Author: Fionn McCarthy

# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float
number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))
