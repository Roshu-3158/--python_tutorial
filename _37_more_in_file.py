f = open("34_write.txt")
# print(f.tell()) # to chake where is our file pointer 
print(f.readline())
# print(f.tell())

f.seek(10) # reset the pointer to the decided position

print(f.readline())
# print(f.tell())

