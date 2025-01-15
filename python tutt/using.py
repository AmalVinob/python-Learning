import datetime
import random

random_num = random.randint(0, 5)
# print(random_num) #print any random number in bw 0 and 5


rand = random.random()
# print(rand) # print in bw 0 and 1 we can multipy it too

lst = ["starplus","cn","star gold","dd1","pogo"]

print(random.choice(lst))


import math

print(math.factorial(5))
print(math.floor(6.998765))
print(math.ceil(6.666))

from datetime import date

print(date.today())
# print(datetime.datetime())

import random
import sys

def random_game():
    rand_num = random.randint(0,10)

    m = int(input("enter the number : "))

    if m > 10:
        print("number is greater than 10 !!!!! \n enter again ")
        random_game()
    else :
        if m == rand_num :
            print(" your guess is correct !!!!")
        else :
            print("try again !!!!!")
            print("random number is   : " ,rand_num)


random_game()




'''another functions
random.randrange()
random.randbyte()
random.Random()

'''


a = random.randrange(5)
random.randbyte()
random.Random()
print(a)