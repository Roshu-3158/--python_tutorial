# it is use to detect execution time
import time

initial = time.time()

k=0
while(k<45):
    print("My name is Roshan")
    time.sleep(2)   # the program should be stop for 2 seconds
    k+=1
print(f"while loop ran in {time.time()-initial} seconds")

initial2 = time.time()
for i in range(45):
    print("My name is Roshan")
print(f"for loop ran in {time.time()-initial2} seconds")


# print the current time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)