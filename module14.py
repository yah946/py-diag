

class Book:
    def __init__(self,title, author, available = True):
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        is_available = "available" if self.available else "borrowed"
        return f"{self.title} of {self.author} is {is_available}"
    def borrow(self):
        self.available = False
    def return_back(self):
        self.available = True

class Member:
    def __init__(self,name,borrowed_books = []):
        self.name = name
        self.borrowed_books = borrowed_books
        
    def borrow_book(self,book):
        if(book.available):
            self.borrowed_books.append(book.title)
            book.borrow()
        else:
            print(f"Error: The book {book.title} isn't available")

    def return_book(self,book):
        self.borrowed_books.remove(book.title)
        book.return_back()
        
    def number_of_books_borrowed(self):
        return len(self.borrowed_books)



# book = Book("Dune", "Frank Herbert")
# print(book)

# book = Book("Dune", "Frank Herbert")
# ali = Member("Ali")
# ali.borrow_book(book)
# print(book)
# print("Number of book borrowed by ali: ",ali.number_of_books_borrowed())

# book = Book("Dune","Frank Herbert")
# ali = Member("Ali")
# omar = Member("Omar")
# ali.borrow_book(book)
# omar.borrow_book(book)

book = Book("Dune", "Frank Herbert")
ali = Member("Ali")
ali.borrow_book(book)
ali.return_book(book)
print(book)
print(ali.number_of_books_borrowed())