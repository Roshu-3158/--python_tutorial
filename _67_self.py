class Employees: 
    no_of_leaves = 8
    
    def info(self):
        return f"My name is {self.name}. i am {self.role} with {self.salary}"

roshan = Employees()
mangesh = Employees()

roshan.name = "roshan"
roshan.salary = 34232
roshan.role = "intern"

mangesh.name = "mangesh"
mangesh.salary = 764354
mangesh.role = "HR"

print(roshan.info())
