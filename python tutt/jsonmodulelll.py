# """
# json - java script object notation
# loads - used to load  string to a js as dictinory
# load,
# dump - used to print js files
# dump - used to write to any other file...
# """
# import json
# data = '{"var1" : "amal", "var2" : "23"}'
# print(data)
# # print(data['var1'])       #TypeError: string indices must be integers
#
# parsed = json.loads(data)
# print(parsed['var1'])
# print(parsed)
#
# # f = open("data","w")
# # data = json.load(f)
# #
# # for i in data["var1"]:
# #     print(i)
# # f.close()
#
#
# print(type(parsed))
# print(type(data))
#
# #json.dump
#
# data2 = {
#     "channel name ": "amal.code",
#     "cars" : ['benz','bmw', "porche", "ferrary"],
#     "fridge" : ('rotti', 540),
#     "afreedi" : False
# }
#
# # jscomp = json.dumps(data2)
# # print(jscomp)
# #
# # jso = open("amal.txt", "w")
# # json.dump(data2,jso, indent=4)
# # jso.close()
# js = json.dumps(data2, sort_keys=True)
# print(js)
