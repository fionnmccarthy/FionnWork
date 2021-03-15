# b. Look at the program below, Assuming the file test-b.txt does not exist, what
#    will be outputted to the console when this program is run?
# c. What will the contents of the file test-b.txt be when this program is run?


# the with statement will automatically close the file
# when it is finished with it
with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)

with open("test-b.txt", "w") as f2: # open file again
    data = f2.write("another line\n") # returns the number of chars written
    print (data)

# b. answer is output: 7 & 13 -- as tehse are number of chars in each line 

# c. answer is "anotehr line" as it will overwrite teh first line written in to file

# d. Look at the modified program below, what will the contents of the file be
#    after this program is run

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)

with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line") # returns the number of chars written
    print (data)

# d. this time it will open the file the second tim in append mode so will output 2 lines - "test d" and "another line"
