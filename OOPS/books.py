
class Book:
    title: str
    author: str
    price: int 
    language: str


    def __init__(self, title, author, price, language): #initializing instance variables

        self.title = title
        self.author = author
        self.price = price
        self.language = language

    def display_book(self):  # Corrected indentation
        print(self.title, self.author, self.price, self.language)


book_instance = Book("Looking for alaska", "John Green", 677, "English")
book_instance.display_book()

