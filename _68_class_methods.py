class employees:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole ): 
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f" My name is {self.name}. any my role is {self.role} with {self.salary} stipend. "

    @classmethod     # this is the class method which can be used as alternatie constructor  
    def change_leaves(cls, new_leaves):  # it chnage the value of class attribute not just the instance attribute 
        cls.no_of_leaves = new_leaves

roshan = employees("roshan", 4321, "intern")

employees.change_leaves(40)   # also instance like roshan also can access this classmethod
print(roshan.no_of_leaves)