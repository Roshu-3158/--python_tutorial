"""
print("enter the first number")
a =int(input())

print("enter the second number")
b =int(input())

if a*b==45*3:
    print("555")
elif a+b==56+9:
    print("77")
elif a/b==56/6:
    print("4")
else:
    c=a+b
print("The addition is " ,int(c))

d=a*b
print("the multiplication is", int(d))

e=a/b
print("the division is " ,float(e))

f=a-b
print("the substraction is" ,int(f))

"""


print("Enter the first Number")
a = int(input())

print("Enter the second Number")
b = int(input())

print("Enter whoch opearation you wants to perform : '+','-','*','/','**' ")
c = input()

if a==45 and b==3 and c=='*':
    print(555)
elif a==56 and b==9 and c=='+':
    print(77)
elif a==56 and b==4 and c=='/':
    print(4)
elif c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
elif c=='**':
    print(a**b)
else:
    print("Something went wrong")
    
    