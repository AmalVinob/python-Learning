import re

mysel = """hello ambani
phoneno : 553533633
fax : +1(752)53354354
tele:+91 54673-234
call : +91 2342352466
website :www.google.com
usa carshore room
sdasldhfakhsdfjkajk  sdc
haihaihaihaiahaiahaiahaiahaiiiiii"""


# findall ,search , split, sub, finditer
# print(r"\n") r string donot let escape character to escape

patt = re.compile(r"room")
# patt = re.compile(r"^hello")
# patt = re.compile(r".room")
# patt = re.compile(r"sdc$")
# patt = re.compile(r"ai*")
# patt = re.compile(r"ai+")
# patt = re.compile(r"ai{2}")
# patt = re.compile(r"(ai){2}")
# patt = re.compile(r'ai{1}|fax')
#
matches = patt.finditer(mysel)
for match in matches:
    print(match)
    # print(mysel[93:97])


# special sequrence

# pattern = re.compile(r'\Ahello')
# pattern = re.compile(r'\bfax')
# pattern = re.compile(r'com\b')
# pattern = re.compile(r'com\b')
# pattern = re.compile(r'\d{5}-\d{3}')
# pattern = re.compile(r'.[+]\d[91][0-9]*')
# pattern = re.compile(r'[+]\d[91]\d{10}\b')

# print(pattern)

# matches = pattern.finditer(mysel)
# for match in matches:
#     print(match)

