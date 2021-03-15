# Write some code to check if the file exists. To do this we will need to import
# os.path and use the isfile() function. You would need to look this up.

import os.path
filename = "count.txt"
if not os.path.isfile(filename): #isfile function checks if the file is there (in current directory)
    print ("File does not exist")
    #initialise file here