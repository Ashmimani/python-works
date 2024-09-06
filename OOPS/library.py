class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author
        

    def __str__(self):
        return self.title

    def print_details(self):
        print(self.title,self.author)

lfa_instance=Book("aadujeevitham","benyamin")
harry_potter_instance=Book("harry potter","JK Rowling")

class Library:
    def __init__(self,name,place):

        self.name=name
        self.place=place
        self.books=[]

    def add_books(self,books):
        self.books.append(books)

    def list_books(self):
        for b in self.books:
            print(b)

library_instance=Library("anjitha","pathanamthitta")
library_instance.add_books(lfa_instance)
library_instance.add_books(harry_potter_instance)
library_instance.list_books()