import random

c1 = 0
b1 = 0
n = 1
while n <= 5:
    a = ["snake","water","gun"]
    b = input("which do you want : ")
    c = random.choice(a)
    print(f"the computer guess is {c}")
    if b in a:
        if c == b:
            print("the guess are same \n nobody got point")
        elif c == "snake" and b == "water" or c == "water" and b == "gun" or c == "gun" and b == "snake":
            c1+=1
            print(f"computer wins the {n}th match")
        else:
            b1+=1
            print(f"you wins the {n}th match")
    else:
        print("you enter the in valid in put :")
        break
    n+=1

if b1 > c1:
    print(f"you win the match with {b1} wins out of 5 matches ")
else:
    print(f"computer wins with {c1} wins out of 5 matches")
