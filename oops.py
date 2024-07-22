import streamlit as st

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
            st.write("The book is unavailable")

    def return_book(self, book):
        if book in self.borrowed_book:
            book.available_copies += 1
            self.borrowed_book.remove(book)
        else:
            st.write("The book is not borrowed")

    def __str__(self):
        return f"The {self.name} (ID: {self.member_id}), Contact: {self.contact_info}"
    
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
                st.write(f"The book with ISBN {ISBN} is removed.")
                return
        st.write("Book not found.")

    def search_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                st.write(f"Book found: {book}")
                return
        st.write("Book not found.")

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                st.write(f"The member with ID {member_id} is removed.")
                return
        st.write("Member not found.")

    def list_books(self):
        for book in self.books:
            st.write(book)

    def list_members(self):
        for member in self.members:
            st.write(member)

def main():
    st.title("Library management system")

    library = Library()

    book1 = Book(st.text_input("1987","George Orwell","2000",1979,5))
    library.add_book(book1)

    member1 = Member(st.text_input("Aishu","1234",1234567890))
    library.add_member(member1)

    member1.borrow_book(book1)
    member1.return_book(book1)


    library.list_books()
    library.list_members()           





