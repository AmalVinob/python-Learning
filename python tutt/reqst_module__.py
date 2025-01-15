# #get and post
# import requests
# r = requests.get("https://financialmodelingprep.com/api/v3/quote-short/AAPL?apikey=YOUR_API_KEY")
# print(r.text)
# print(r.status_code)

import requests

paylod = {"firstNAme" : "johm", "lastName" : "Smith"}
r = requests.get("https://httbin.org/get", params=paylod)
# print(r.url)
# print(r.status_code)
# print(r.content)
# print(r.text)

#post request
# used when submitiing from html or uploading files

paylod = {"firstNAme" : "johm", "lastName" : "Smith"}
r = requests.post("https://httbin.org/post", data=paylod)
# print(r.url)
print(r.text)