list_1 =[1,2,3,4,5,6,7,8,9]

def is_greter_5(num):
    return num > 5

is_greter_5 = list(filter(is_greter_5,list_1))
print(is_greter_5)