# guessextra.py
# Lab Week 4 part 2
# Fionn McCarthy
# get the program to generate a random number between 0 and 100 to guess


import random
numberToGuess = random.randint(1,100)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
