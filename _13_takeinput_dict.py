
from multiprocessing.sharedctypes import Value


my_dict={"name":"roshan" ,
         "village":"askheda",
         "taluka":"satana", 
         "district":"nashik" }

print("Enter which information you want about RN")
a =input()
print(my_dict[a])

