# recursive : A program is called recursive when an entity calls itself.
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number : "))
print("factorial using recursive method : ",factorial_recursive(number))