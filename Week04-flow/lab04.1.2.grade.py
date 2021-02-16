# grade.py
# Lab Week 4
# Fionn McCarthy
# The below program reads in a students percentage mark and
# prints out corresponding the grade (the program should check that the
# percentage is valid:
# Under 40% => Fail
# Between 40% and 49% => Pass
# Between 50% and 59% => Merit 2
# Between 60% and 69% => Merit 1
# Over 70% => Distinction

percentage = float(input("Enter the percentage: "))
#print (percentage)
# be careful with ands and ors
if percentage < 0 or percentage > 100:
 # Later we will show you error handling
 # This should really throw an error 
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
    print ("Fail")
elif percentage < 50: # 40 to 49
    print ("Pass")
elif percentage < 60: # 50 to 59
    print ("Merit1")
elif percentage < 70: # 60 to 69
    print ("Merit2")
else: # else would be between 70 and 100
    print ("Distinction")