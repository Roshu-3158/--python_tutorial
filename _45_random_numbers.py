# random module rand = random.random()
import random

# for generating random numbers form 0 to 100
random_numbers = random.randint(0,100)
print(random_numbers)  

# generating numbers from 0 to 1
rand = random.random()
print(rand)

# generating numbers from 0 to 100
rand2 =random.random() * 100
print(rand2)

# selecting random from the list 
fruits =["mango","grapes","pineapple","apple","banana"]
choose = random.choice(fruits)
print(choose)