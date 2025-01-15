# function caching
# --------------------------


import time
from functools import lru_cache #lru cache is a decorator

@lru_cache(maxsize=3) # it saves the latest 3 cacheee ie in last line
def some_work(n):
    #some task taking n time
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("now runnimg some work ")
    some_work(3)
    some_work(1)
    some_work(2)
    some_work(9)
    print("done..... calling again...")
    some_work(5)
    input()
    some_work(3)
    print("called again")


"""
it saves the latest 3 cacheee ie somework(1),(2),(9),then print ... then saves latest 3 value ie somework(9),(5),(3)
"""