def searcher():
    import time
    #some time consuming task
    book = " this is a book on amal and code with amal ....."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("text is in the book")
        else:
            print("text is not on the book")

search = searcher()
next(search)
search.send("amal")

# search.close()   for closing search

input("press any key : ")
search.send("nklasf and")
input("press any key : ")
search.send("alksdhfk")
input("press any key : ")
search.send("amdc")
input("press any key : ")
search.send("this is ")


search.close()
"""
coroutines are used when there is a task in your function which takes more time
for reading machine learning module,,,,,,,,,,,
"""