class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybooks(self):
        print(f"we have following books in our library !!!! {self.name}")
        for books in self.booklist:
            print(books)

    def lendbook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender - book data base has been updated . you can take the book")
        else :
            print(f"book is already beeing used by {self.lendDict[book]}")

    def addbook(self,  book):
        self.booklist.append(book)
        print("book has been added !!!!!!!")

    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    amal = library(['python','rich daddy','c++','poor daddy',"harry poter"],"codewithamal")

    while True:
        print(f"welcome to the {amal.name} library. enter your choice to continue ")
        print("1. dislay books ")
        print("2. lend books ")
        print("3. add books ")
        print("4. return book ")
        user_choice = int(input("enter your choice_number :"))

        if user_choice == 1:
            amal.displaybooks()

        elif user_choice == 2:
            book = input("enter the name of the book you want tot lend : ")
            user = input("enter your name : ")
            amal.lendbook(user, book)

        elif user_choice == 3:
            book = input("enter the name of the book you want to add : ")
            amal.addbook(book)

        elif user_choice == 4:
            book = input("enter the name of the book you want to return : ")
            amal.returnbook(book)


        else :
            print("not a valid option:")

        print("press q to quit and c to  continue :")
        user_choice2 = input("enter q/c : ")
        while(user_choice2 == "c" and user_choice2 == "q"):
            if user_choice2.lower() == "q":
                exit()
            elif user_choice2.lower() == "c":
                continue




