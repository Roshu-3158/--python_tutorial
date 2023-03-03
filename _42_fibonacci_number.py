# 0 1 1 2 3 5 8 13 21  fibonacci series 

def function1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return function1(n-1) + function1(n-2)
number = int(input("enter the number : "))
print("the Fibonacci number :  ",function1(number))
