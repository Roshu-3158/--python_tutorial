from functools import reduce #reduce is the function of functools module

# ordinarry way to print sum of all elements in list 1+2+3+4 = 10
# list1 =[1,2,3,4]
# num = 0
# for i in list1:
#     num = num +i
# print(num)


# more efficient way using reduce 

list1 =[1,2,3,4]

num = reduce(lambda x,y:x+y,list1)
print(num)

