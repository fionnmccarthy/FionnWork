# sub.py
# Lab 2.3  Types: Part 2
# This program reads in two numbers and subracts the first one from the second one
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
# author: Fionn McCarthy

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))
