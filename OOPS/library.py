class Book:

    def _init_(self,title,author):
        self.title=title
        self.author=author
        

    def _str_(self):
        return self.title

    def print_details(self):
        print(self.title,self.author)

lfa_instance=Book("looking for alaska","John Green")
harry_potter_instance=Book("harry potter","JK Rowling")

class Library:
    def _init_(self,name,place):
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