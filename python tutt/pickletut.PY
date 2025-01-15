"""
pickle used for read and write anything into binary format
dump is used to dump a list into file
dumps used not to store or retrive dara but to shoew the list or anything in bye formate
load is used for load the binary file into list......
loads is used to transfer byte object into list format..... 
"""

import pickle

# picking a pythonobject
cars = ["audi", "bmw", "benz", "amalty"]

# with open("mycar.pkl","wb") as f:
#     fileobj = pickle.dump(cars,f)

file = open("mycar.pkl","rb")
fileobj = pickle.load(file)
print(fileobj)
print(type(fileobj))

f = pickle.dumps(cars)
print(f)

k = pickle.loads(f)
print(k)