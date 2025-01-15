def searcher():
    f = open("file3.txt")
    opener = f.read()

    while True:
        text = (yield)
        if text in opener:
            print(f"your name was found in letter {f.readline()}")
        else:
            print("your name was not found !!!!")

search = searcher()
next(search)
search.send(input("enter the name : "))

search.close()