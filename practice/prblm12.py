class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True   
    
    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f'{self.book_id}: {self.title} by {self.author} ({status})'
    
class Library:
    def __init__(self):
        self.items = []
    
    def add_book(self, book):
        self.items.append(book)
        print(f'{book.title}: added successfully')

    def remove_book(self, id):
        for book in self.items:
            if book.book_id == id:
                self.items.remove(book)
                print(f'Book deleted: {book.title}')
                return
        print('Book not found')
    
    def search_book(self, title):
        for book in self.items:
            if book.title.lower() == title.lower():
                print('Book found', book)
                return book
        print("Book not found")
        return None

    def borrow_book(self, id):
        for book in self.items:
            if book.book_id == id:
                if book.available:
                    book.available = False
                    print(f'You borrowed: {book.title}')
                else:
                    print('Book not available')
                return
        print("Book not found")
    
    def return_book(self, id):
        for book in self.items:
            if book.book_id == id:
                if not book.available:
                    book.available = True
                    print(f'Book returned: {book.title}')
                else:
                    print('This book was not borrowed')
                return
        print('Book not found')
    
    def show_all_books(self):
        if not self.items:
            print("No books in the library")
            return
        for book in self.items:
            print(f'{book.title}')

b1 = Book(1, 'Twinkle', 'Rishab')
b2 = Book(2, 'Stars in the night', 'Girish')
b3 = Book(3, 'Everthing happens for a reason', 'GOD')
b4 = Book(4, 'Be patient', 'God')

library = Library()

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
# library.show_all_books()
library.search_book('Stars in the night')
library.borrow_book(3)
library.borrow_book(2)
library.borrow_book(3)
library.remove_book(1)
library.show_all_books()