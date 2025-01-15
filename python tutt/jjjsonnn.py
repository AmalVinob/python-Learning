"""
java script object notation......
dumps used to make a json as string


"""
# import json

# people_list = '''
# {
#     "people" : [
#      { "name" : "smith",
#        "place" : "UK",
#        "email" : "smith66@gmail.com",
#        "phone" : "919156982",
#        "licence" : false
#      },
#      {
#        "name" : "amal",
#        "place" : "india",
#        "email" : "amalvinob@gmail.com",
#        "phone" : "452463465432",
#        "license" : true
#      }
#      ]
# }
# '''
#
# print(people_list)
#
# data = json.loads(people_list)
# print(data)
# # print(data['people'])
# print("\n\n")
# # for person in data['people']:
# #     print(person)
# #     print(person['name'])
#
# for person in data['people']:
#     del person['phone']
#
# newstring = json.dumps(data, indent=2, sort_keys=True)
#
# print(newstring)

# with open("amal.txt") as f:
#     data = json.load(f)
#
# for state in data['people']:
#     print(state['name'],state['phone'])
#
# for state in data['people']:
#     del state['place']
#
# with open("json_place.json", "w") as f:
#     json.dump(data, f, indent=2)



import json
from urllib.request import urlopen
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
print(source)