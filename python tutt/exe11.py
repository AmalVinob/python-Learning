a = """hello ambani
phoneno : 553533633
fax : +1(752)53354354
tele:+91 54673-234
call : +91 2342352466
website :www.google.com
usa carshore room
sdasldhfakhsdfjkajk  sdc
sar : amal552@gmail.com
k : athul@gmail.com
amal
haihaihaihaiahaiahaiahaiahaiiiiii"""

import re

# patt = re.compile(r'[\w.]+[@][\w.]+')
# math = patt.findall(a)
# for i in math:
#     print(i)


# mail = re.compile(r'[\w]+[@][\w.]+')
# math = mail.findall(a)
# for i in math:
#     print(i)


email = re.findall(r"[0-9a-zA-Z.+_%]+@[0-9a-zA-Z.]+[.][a-zA-Z0-9]+",a)
print(email)

gmail = re.findall(r"\w+@\S+\w",a) # \w = 0-9a-zA-Z.+_%, \S = no while spaces
print(gmail)
