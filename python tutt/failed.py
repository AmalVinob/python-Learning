def book(self, wanter):
    while True:
        question = input(f"do you want to {wanter} ? yes or no : ")
        if question.lower() == "yes":
            if wanter == "add":
                a = input("enter the name of the book : ")
                b = input("enter the name of the author : ")
                self.books.update({a: b})
                print(self.books)
            elif wanter == "lend":
                a = input("enter the name of the book : ")
                b = self.books.get(a)
                if a in self.books:
                    print("greate the book is present !!!")
                    lended = {}
                    lended.update({a: b})
                    print(lended)
                    self.books.pop(a)
                    print(self.books)
                else:
                    print("the book you enterd is not in the library !!!!!")
            elif wanter == "return":
                a = input("enter the name of the book : ")
                if a in lended:
                    pass
        else:
            break
