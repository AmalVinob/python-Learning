import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k == 1:
        c = int(input("enter 1 for exersise and 2 for food"))
        if c == 1:
            value = input("enter exersice here !!!!")
            with open()