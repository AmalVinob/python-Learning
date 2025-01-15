dictnory = {}
for i in range(1,3):
    name = input("enter the name of word : ")
    meaning = input("enter the meaning of word : ")
    dictnory.update({name : meaning})


print(dictnory)
for i in dictnory:
    print(i)