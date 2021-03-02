# lab06 part 4 doAdd
# Lab Week 06
# Fionn McCarthy

def readModules():
    return []


def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)


#test
students = []
doAdd(students)
doAdd(students)
print (students)
