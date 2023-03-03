# stone paper scissor game 
import random
i = 0
c=[]
d=[]
print("The total score is present after playing it 10 times")
for i in range (0,10):
    print("Enter your choice : stone paper scissor : ",end="")
    a = str(input())

    print(f"you choose {a} option")

    game = ["stone", "paper", "scissor"]
    b = random.choice(game)
    print("computer Choose",b)
    
    
    if a=="stone" and b=="stone":
        c.insert(1,"1")
        d.insert(1,"1")
        print("Match tie")
    
    elif a=="stone" and b=="paper":
        d.insert(2,"2")
        print("Computer win")
    
    elif a=="stone" and b=="scissor":
        c.insert(2,"2")
        print("You win")

    elif a=="paper" and b=="stone":
        c.insert(3,"3")
        print("You win")
    
    elif a=="paper" and b=="paper":
        d.insert(3,"3")
        c.insert(4,"4")
        print("Match tie")
    
    elif a=="paper" and b=="scissor":
        d.insert(4,"4")
        print("Computer win")

    elif a=="scissor" and b=="stone":
        d.insert(5,"5")
        print("Computer win")
    
    elif a=="scissor" and b=="paper":
        c.insert(5,"5")
        print("You win")
    
    elif a=="scissor" and b=="scissor":
        c.insert(6,"6")
        d.insert(6,"6")
        print("Match tie")

    print()


print("Your total points = ",len(c))
print("Computer total points= ",len(d))

if len(c) > len(d):
    print("Congratulations ! you win")
    print(f"You win by {len(c)-len(d)} points")
    
elif len(d) > len(c):
    print("You lose")
    print(f"Computer win by {len(d)-len(c)} points")

elif len(d) == len(c):
    print("Match tie")


    


    


