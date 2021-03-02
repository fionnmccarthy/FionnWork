# lab06 part 5 read_in_modules
# Lab Week 06
# Fionn McCarthy


def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print (students)