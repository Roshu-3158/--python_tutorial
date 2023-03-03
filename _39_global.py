"""
l = 10  #global variable 
def function1(r):
    # l =5  #local variable 
    # print(l)  # printing local variable
    print(r,"my name start with r") 
    global l  # it gives the permission to change the value of global variable inside the function
    l = l +45
function1(int(input("Enter the number: ")))
print(l)  # printing global variable 

"""


# gloabl keyword change outer variable which is not a subpart of any function 

r=21
print("The value of r before calling any function: ",r)
def roshan ():
    r =31
    def roshu():
        global r
        r = 58 
        print("before calling roshu()",r)
    roshu()
    print("after calling roshu()",r)
roshan() # call the roshan function
print("r: ",r)
 
