# normalise.py
# Lab 3.3  Part 2
# This program takes in a string and strips any leading or trailing spaces,
# the program should also convert the string to lower case.
# Author: Fionn McCarthy

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print("That String normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised ))