# take a list and chake the int in the list and print the number which is larger than 6

dict = ["dg","roshan","nikam", 54, 56,5,4,1,65]

for item in dict:
    if str(item).isnumeric() and item>6:
        print(item)