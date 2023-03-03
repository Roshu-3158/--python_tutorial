# recoraters in python 

def dec1(func1):    #dec1 function takes func1 function as a argument 
    def nowexec():
        print("Executing now")
        func1()   # func1 executed 
        print("Executed")
    return nowexec

@dec1     # ----> using decorator in python 
def who_is_roshan():
    print("Roshan is good boy ")

# who_is_roshan = dec1(who_is_roshan)  ----> ordinary way

who_is_roshan()