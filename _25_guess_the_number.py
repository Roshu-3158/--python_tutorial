# guess the number and also gave the suggetion if guess number is greater than original number or smaller than original number 

while(True):
    print("Enter the number")
    a = int(input())
    b=31
    if a>b:
        print("you enter too large ! take it less")
    
    elif a<b:
        print("you enter too less ! take it greater ")

    else:
        print("Congratulations you entered correct suggetion")
        break
        