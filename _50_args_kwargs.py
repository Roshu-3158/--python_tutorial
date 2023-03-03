# arguments send in the form of tuples
# arcs argument must be passed after the normal argument 
def funargs(normal,*args,**kwargs):   
    print(normal)
    for item in args:
        print(item) 
    print()
    print("We are intoducing")
    for key,value in kwargs.items():
        print(f"{key} is a {value} of our class")

rn=["roshan","manoj","mangesh","pravin"]
normal = "I am a normal argument this student are :"
kwargs ={"roshan":"monitor", "manoj":"environment_instructor", "mangesh":"programmer", "pravin":"tester"}
funargs(normal, *rn, **kwargs) 

# You can use *args and **kwargs as arguments of a function when you are unsure about the number of arguments to pass in the functions.