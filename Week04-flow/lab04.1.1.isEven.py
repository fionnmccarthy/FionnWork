# isEven.py
# Lab Week 4
# Fionn McCarthy
# The below number uses an if else statement to check if a number is even or odd


number = int(input("enter an integer:"))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))