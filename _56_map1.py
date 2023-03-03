# we wants to convert all the numbers in int which has previously string 

numbers = ["43","32","43","76","93"]

# we can typecast using map functin like this 
numbers = list(map(int,numbers))   # firstly we convert it into a list 

# this is the ordinaary way of typecasting 
# for i in range(len(numbers)):
#     numbers[i]= int(numbers[i])

numbers[2] = numbers[2] + 10
print(numbers[2])



