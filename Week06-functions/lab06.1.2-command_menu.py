# lab06 part 2 command_menu
# Lab Week 06
# Fionn McCarthy

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
#test the function
choice = displayMenu()
print("you chose {}".format(choice))