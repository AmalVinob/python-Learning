a = int(input("how many item do you want to enter : "))
l =[input("enter the value : ") for i in range(1,a+1)]
b = input("which comprehension ddo you want : list or dictionary or set ? : ")

if b.lower() == "list":
    print([item for item in l])
elif b.lower() == "dictinory":
    print({item : input(f"the value of {item}") for item in l})
elif b.lower() == "set":
    print({item for item in l})
else :
    print("invalidy syntax !!!! try again")