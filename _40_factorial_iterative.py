#iterative : A program is call iterative when there is a loop (or repetition).

# factorial of 5 = 5*4*3*2*1

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

number = int(input("Enter the number :"))
print("Factorial using iterative method : ",factorial_iterative(number))