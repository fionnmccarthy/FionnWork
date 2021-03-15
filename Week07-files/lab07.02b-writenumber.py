# b. Write a function that takes in a number and overwrites a file with that
# number (count.txt). test it and check that the file has been changed

filename = "count.txt"

def writeNumber(number):
    with open(filename, "wt") as f: # 'w' will open/create a file for writing; 't' is for text mode
        # write takes a string so we need to convert
        f.write(str(number)) # f.write is teh write command

# test it
writeNumber(3)
