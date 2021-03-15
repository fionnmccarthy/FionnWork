# a. Write a function that reads in a number from a file that already exists
# (count.txt). test the program by calling the function and outputting the number


filename = "count.txt"
def readNumber():
    with open(filename) as f: # mode 'r' is default mode so reads 
        number = int(f.read()) # f.read reads first line of file 
        return number

# test it
num = readNumber()
print (num)
