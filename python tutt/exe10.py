# r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# import requests
# import pickle
#
# with open("iris.data") as f:
#     data = f.read().splitlines()
#
# # for i in data:
# #     print(i)
# file = "iris.pkl"
# with open(file,"wb") as fileobj:
#     pickle.dump(data,fileobj)
#
# with open('iris.pkl','rb') as fileobj1:
#     read = pickle.load(fileobj1)
# for item in read:
#     print(item)

#
# import pickle
# with open("iris.data") as f:
#     data = f.read().splitlines()
# # for i in data:
# #     print(data)
#
# file = "iris.pkl"
# with open(file,"wb") as fileobj:
#     pickle.dump(data, fileobj)
#
# with open(file,"rb") as fileobj1:
#     read = pickle.load(fileobj1)
#
# for item in read:
#     print(item)

# import requests
# data = requests.get("enter the url").text
# print data

import pickle
with open("iris.data") as f:
    data = f.read().split("\n")
    print(data)

l2 = [item.split(",") for item in data]
print(l2)

with open("iris.pkl", "wb") as f:
    pickle.dump(l2,f)

with open("iris.pkl", "rb") as f :
    print(pickle.load(f))