# writing in a file
"""
f = open("34_write.txt", "w")
f.write("i am a good boy !")
f.close() 
"""

# append in a file 
"""
f = open("34_write.txt", "a")
f.write("i am a good boy ! \n")
f.close()
"""

# handle write and read both 
f = open("34_write.txt", "r+")
print(f.read()) 
f.write("i am a good boy r !")
f.close() 






