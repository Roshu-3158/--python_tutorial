l1 = ["roshan","manoj","pravin","mangesh"]

for index, item in enumerate(l1):    # we can access index with the help of enumerate
    if index%2==0:
        print(f"{item} is selected")