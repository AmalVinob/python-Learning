l = [i for i in range(100) if i%3 ==0]
print(l)
"""
not only list there are dictonary and other comprehencions are there

"""

#dictonary comprehension

dict = {i:f"item{i}" for i in range(10)}
print(dict)

# dict1 = {input("enter the key"):input("enter the value") for i in range(5)}
dict1 = {i : f"Item {i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)

"\n"

#set comprehencion

dresses = {i for i in range(1,10)}
print(type(dresses))
print(dresses)

dresse = {dress for dress in ["dress1", "dress2","dress1", "dress2","dress1", "dress2"]}
print(dresse)

#it will print dress1 and dress2 because it is set comprehencion

dresse = [dress for dress in ["dress1", "dress2","dress1", "dress2","dress1", "dress2"]]
print(dresse)
# if it is list comprehension then it will print every element on the list

# generator comprehension

even = (i for i in range(100) if i%2 ==0)
print(type(even))
# print(even.__next__())
# print(even.__next__())
# print(even.__next__())

for item in even:
    print(item)