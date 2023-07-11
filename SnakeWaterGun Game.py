

import random
print("Here's the snake,water,gun game\n")



i=0
while(i<10):

    l1 = ["snake", "water", "gun"]
    a = random.choice(l1)
    print(a)

    b = str(input(" Write your choice\n"))
    if a=="snake" and b=="water":
        print("snake will drink water.. you lose")
        continue

    elif a=="snake" and b=="gun":
        print("gun kills snake.. you won")
        continue

    elif a == "snake" and b == "snake":
        print("Tied")
        continue

    elif a=="water" and b=="gun":
        print("gun drowned in water.. you lose")
        continue

    elif a == "water" and b == "snake":
        print("snake drinks water.. you won")
        continue

    elif a == "water" and b == "water":
        print("Tied")
        continue

    elif a == "gun" and b == "water":
        print("gun drowned .. you won")
        continue


    elif a == "gun" and b == "snake":
        print("snake is killed.. you lose")
        continue


    elif a == "gun" and b == "gun":
        print("Tied")
        continue

    # else:
    #     print("None")

i=i+1

if i>10:
    print("GAME OVER")

print("How many times you played")


