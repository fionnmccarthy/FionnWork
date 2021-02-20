# guess1.py
# Lab Week 4 part 2
# Fionn McCarthy
# prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on

numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
    print ("Well done! Yes the number was ", numberToGuess)

print ("Well done! Yes the number was ", numberToGuess)
