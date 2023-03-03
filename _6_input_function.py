# always remeber while taking input in python the input is always taken in the form of string.

from cgi import print_form


print("Enter the first number : ")
a = input()
print("Enter the second number : ")
b = input()

print("here the strings are added",end=" ")
c= a+b
print(c) # here the output is printed as a string 

print("here the int are added", end=" ")
c= int(a)+ int(b)
print(c) # typecast the c in int 
