def sqaure(a):
    return a*a

def cube(a):
    return a*a*a

ref =(sqaure,cube)

for i in range(5):
    num = list(map(lambda x:x(i), ref))
    print(num)