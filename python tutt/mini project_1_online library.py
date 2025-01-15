'''

library management system
--------------------------------
create library class
1st method to desplay book
              lend book = who ownes  the book if not present in librsry
              add book
              return book


amal library = library (listof books, library name)

dictonery =  book - name of person

create a main function and run an infinte while looop asking users  for their input

'''

class library:
    def __init__(self,listofbooks,library_name):
        self.books = {"atomic habit":"amal" , "gridy man":"athul","mistakes":"anu"}
        self.listofbooks = listofbooks
        self.library_name = library_name
    def display_book(self):
        # c = self.books.keys()
        # d = self.books.values()
        print("book name       author name\n---------------------------- ")
        for i in (self.books):
            print(f"{i}         {self.books[i]}")

    def add_book(self):
        question = input("do you have any book to add : yes or no :")
        if question.lower() == "yes":
            a = input("do you want to add book \n enter the name of the book : ")
            b = input("enter the name of the author : ")
            self.books.update({a : b})
            print(self.books)
            self.display_book()
    def lend(self):
        question = input("do you have any book to lend : yes or no : ")
        if question.lower() == "yes":
            a = input("enter the name of the book : ")
            for i in self.books.keys():
                if a == i:
                    print("greate the book is present !!!")
                    lended = {}
                    lended.update({a: self.books.get(a)})
                    print(lended)
                    self.books.pop(a)
                    self.display_book()
                    print(self.books)
                    return lended

    def return_book(self):
        question = input("do you have any book to return : yes or no :")
        if question.lower() == "yes":
            a = input("enter the name of the book : ")
            lended = self.lend()
            for i in lended.keys():
                if a == i:
                    print("are you here to return .... then let me have it \n i have stored it again in the library thanku visit again !!!!")
                    self.books.update({a : self.books.get(a)})
                    print(self.books)
                    self.display_book()
                else :
                    print(" this is not our book!!!!")




Amal_library = library("list_of_books","Amal_library")
print(Amal_library.display_book())
# print(Amal_library.book(input("what do you want ? lend or add or return")))
print(Amal_library.add_book())
print(Amal_library.lend())
print(Amal_library.return_book())
