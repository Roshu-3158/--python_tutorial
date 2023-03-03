
print("enter a number 1")
num1 = input()

print("enter a number 2")
num2 = input()

try:
    print("the sum of these two numbers is ", int(num1)+int(num2))
except Exception as e:
    print(e)

print("THANK YOU FOR USING MY PROGRAM ")