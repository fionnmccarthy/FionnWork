# div.py
# Lab 2.3  Types: Part 3
# This program reads in two numbers and divides the first one by the second 
# and give the integer result and the remainder
# author: Fionn McCarthy

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = x%y # % gives the remainder
print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder))
