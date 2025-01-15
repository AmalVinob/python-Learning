n = 18

i=1
guess = 9
while(i<=9):
    num = int(input("enter your guess : "))

    if num == n:
        print("you have entered write number !!!")
        print("number of guess yiou take is  : ",i)
        break
    else:
        guess -= 1
        print("the guess is wrong !!!!")
        print("number of guess left  is ",guess)
        if guess == 0:
            print("you loss !!!!")
            break
