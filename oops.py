class Book:
    def __init__(self, title, author, ISBN, year, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.year = year
        self.available_copies = available_copies

    def __str__(self):
        return f"The {self.title} by {self.author} (ISBN: {self.ISBN}) year: {self.year} (available copies: {self.available_copies})"
class Member:
    def __init__(self, name, member_id, contact_info):
        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info
        self.borrowed_book = []

    def borrow_book(self, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.borrowed_book.append(book)
        else:
            print("The book is unavailable")

    def return_book(self, book):
        if book in self.borrowed_book:
            book.available_copies += 1
            self.borrowed_book.remove(book)
        else:
            print("The book is not borrowed")

    def __str__(self):
        return f"The {self.name} (ID: {self.member_id}, Contact: {self.contact_info})"
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print(f"The book with ISBN {ISBN} is removed.")
                return
        print("Book not found.")

    def search_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                print(f"Book found: {book}")
                return
        print("Book not found.")

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"The member with ID {member_id} is removed.")
                return
        print("Member not found.")

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)

library = Library()

book1 = Book("1984", "George Orwell", "1234567890", 1990, 5)
library.add_book(book1)

member1 = Member("Alice", "1", "alice@example.com")
library.add_member(member1)


member1.borrow_book(book1)
member1.return_book(book1)


library.list_books()
library.list_members()




