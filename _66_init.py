class Employees: 
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):   # this is constructor and __int__ used in py for constuctor 
        self.name = aname
        self.salary = asalary
        self.role = arole

roshan = Employees("roshan", 34232, "intern")

print(roshan.salary)