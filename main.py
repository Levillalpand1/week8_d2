
from random import randint
from random import shuffle
from random import choice
# random
# Python comes with a built in random library. There are a lot of functions included in this random library, so we will only  #show you two useful functions for now.
# print("random")
# dice1=randint(1,7)
# print(f"dice1:{dice1}")
# dice2=randint(1,7)
# print(f"dice2:{dice2}")
# rolledDoubles = dice1 == dice2
# if rolledDoubles:
#    print("you rolled doubles!")
# else: print("not doubles")

# if dice1 and dice2==1:
#   print("you rolled snake eyes")
# else: print("you didn't roll snake eyes!")

# my_list=range(1,51)
# print ("my new list")
# print(list(my_list))
# my_list= list(my_list)
# (shuffle(my_list))
# print(my_list)

random=randint(1,201)
print("random")
print(random)

if random % 2== 0:
  print("even numeber!")
else:
  print("odd number")

for num in range(2,201):
  if num % 2==0:
    print(num)
color=["red","blue","pink","purple"]
random_color= choice(color)
print(f"random color is {random_color}")