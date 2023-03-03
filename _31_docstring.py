# docstring is nothing nut the first line which is writeen after the function

def function1(a,b):
    """This is the user defined addition program"""   # this is not a comment it is docstring
    c=a+b
    print(c)
    return c
    
print(function1.__doc__)
a = int(input("enter the first number "))
b = int(input("enter the second number "))
function1(a,b)
