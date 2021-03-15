# a. Look at the program below, assuming that the file test-a.txt does not exist.
# What will happen when the program runs?


# the with statement will automatically close the file
# when it is finished with it
with open("test-a.txt") as f:
 data = f.read()
 print (data)
# this is the same as
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()

# Answer
# the file does not exist so it will not run as will not be able to read the file. 