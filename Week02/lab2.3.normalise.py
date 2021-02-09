# normalise.py
# Lab 2.3  Types: Part 5
# This program reads in a string and strips any leadingor trailing spaces 
# The program should also convert the string to lower case.
# The program should also output the length of the input and output strings
# author: Fionn McCarthy

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print("That String normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(
lenghtOfRawString, lenghtOfNormalised ))