class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return f"Book: {title}, Author: {book.author}"
        return f"There is no such book"


book1 = Book('test1', 'A')
book2 = Book('test2', 'A')
book3 = Book('test3', 'A')

books = Library([book1, book2,book2])
print(books.find_book("test1"))
print(books.find_book("test"))


