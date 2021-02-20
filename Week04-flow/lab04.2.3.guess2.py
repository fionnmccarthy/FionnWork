# guess2.py
# Lab Week 4 part 2
# Fionn McCarthy
# prompts the user to guess a number
# program tells the user if there guess is too high or too low, each time they guess

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: # I know it cant be equal or too low, so it must be too high
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
