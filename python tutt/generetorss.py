"""
itrable -- __iter() or get item__()
itrator -- __next()
itration




generator is also an itretor which we can itrate once --- saves ram
we use yield(ie insted of print and return)` and __next__() function for generator
"""

# for i in range(75):
#     print(i)
# range is alo a generator

def gen(g):
    for i in range(g):
        yield i

g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)

#itreble

A = "amal"
i = iter(A)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())