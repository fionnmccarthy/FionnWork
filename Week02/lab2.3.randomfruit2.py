# randomfruit2.py
# Lab 2.3  Types: Part 7
# This program  prints out a random fruit
# author: Fionn McCarthy

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))