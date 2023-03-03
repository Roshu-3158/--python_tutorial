# lambda functions or anonymous  functions 

# def minus(x,y):
#     return x-y


# minus = lambda x,y : x-y  #lambda function is basically a single line function 


# print(minus(9,4))


# sort method using lambda function

a=[[1,14], [5,6], [8,23]]
a.sort(key=lambda x:x[0])  #sort by index value x[0] position of x
print(a)