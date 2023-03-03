# instance and class variables 

class Employees: 
    no_of_leaves = 8
    pass

roshan = Employees()
mangesh = Employees()

roshan.name = "roshan"
roshan.salary = 34232
roshan.role = "intern"

mangesh.name = "mangesh"
mangesh.salary = 764354
mangesh.role = "HR"

print(Employees.no_of_leaves)
print(roshan.__dict__)    # it simply return a dictonary which contain all infomation
roshan.no_of_leaves = 10  # it simply create the instanse of object roshan and change value in it 
print(roshan.__dict__)    # it simply return a dictonary which contain all infomation
print(Employees.no_of_leaves)