mystr="I am a programmer"
mystr2="mynameisroshan"

# print the string 
print(mystr)

# select the letters with we wants to print(0 to 10)
print(mystr[0:10])

# count the length of the string 
print(len(mystr))

# to skip 1 char and then print
print(mystr[0:15:2])

# chake were string is alpha (chakes were all characters are alphabet *the spaces are not considered)
print(mystr2.isalpha())  #it returns true or false

# chake were string is alpha or numeric
print(mystr.isalnum())

# chake were string end with "programmer"
print(mystr.endswith("programmer"))

# count the characters
#print(mystr.count("am"))

# capatalize the string
#print(mystr.capitalize())

# find the word in string
print(mystr.find("am"))

# convert the string into lower case
print(mystr.lower())

# convert in uppercase
print(mystr.upper())

# replace one word by second
print(mystr.replace("a" , "you"))