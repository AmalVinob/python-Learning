# F strings

# me = "harry"
#
# a = "this is %s " %me
#
# print(a)

import math

me = "amal"
al = 3
# a = "this is {1} {0}".format(me, al)
# print(a)

a = f"this is {me} {al} {10*3} {math.factorial(5)} "

print(a)