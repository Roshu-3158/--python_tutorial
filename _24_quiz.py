while(True):  #true is compulsory used in while loop in python
    print("Enter the number")
    a = int(input())
    if a>100:
        print("you entered number greater than 100")
        break
    else:
        print("try again")
        continue