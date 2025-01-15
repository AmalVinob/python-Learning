from functools import lru_cache
import time

n = input("how many cache you can to save ????")

@lru_cache(maxsize= 5)
def some_work(n):
    #some task taking n time
    time.sleep(n)
    return n

print("helo")
some_work(3)
print("hai")
some_work(4)
some_work(2)
some_work(1)
print("you moron !!!")
some_work(3)
print("you moron !!!")
