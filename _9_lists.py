#list operations 
# the list is mutable ( can change )
# the list is craeted using [] sqauare brackets 


products = ["mobile", "earphones", "tablets", "laptops"]
print(products) # printing whole list in python 
print(products[3]) # printing specific position in the list 

numbers = [54,65,76,87]
print(sum(numbers))  # adding whole nubers in the list 

numbers.sort # sorting the list in ascending order
print(numbers) 

print(numbers[0:2]) # printing specific position numbers in list (*position [2] is not considerd)

numbers.append(65) # append is nothing but add the element in the list at last
print(numbers)

numbers.pop(1) # append is nothing but remove the element in the list. 
print(numbers)
