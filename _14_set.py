s = set() # set is written in round brackets ()
print(type(s)) # printing the type of the list 

s_from_list = set([2,4,6,8,10]) # the better way to make a set is using the list 
print(s_from_list) 

# adding the element is the set
# set use unique values , it didnt repeat the values 
#s = set()
#s.add(36) 
#print(s)
#s.remove(36)     it remove the element
#print(s)


#union of set
s1 = s.union({43,53,4,65})
#print(s1)

#intersection of set 
#s1 = s.intersection({43,53,4,2,65})
print(s,s1)

#length of list 
print(len(s1))

#max value
print(max(s1))

#min value
print(min(s1))
