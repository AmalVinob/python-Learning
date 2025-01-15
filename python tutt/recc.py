# reccursion means functions inside another function
#
# def factorial_itrative(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i + 1)
#     return fact
#
# numb = int(input("enter the number : "))
# print(factorialitrative(numb))
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

# fibinocci 0 1 1 2 3 5 8 13

def fibbinocci(n):
    if n== 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbinocci(n-1) + fibbinocci(n-2)

print(fibbinocci(5))