from orm.models import Author, Book
from orm.database import Base, SessionLocal
from utils import clear_screen, validate_input

def add_book(session):
    clear_screen()
    print("Add a New Book")
    print("================")
    title = validate_input("Enter the title of the book: ", lambda x: len(x) > 0)
    author_name = validate_input("Enter the name of the author: ", lambda x: len(x) > 0)

    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    book = Book(title=title, author_id=author.id)
    session.add(book)
    session.commit()
    print(f"Book added successfully!")

def add_author(session):
    clear_screen()
    print("Add a New Author")
    print("=================")
    name = validate_input("Enter the name of the author: ", lambda x: len(x) > 0)

    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Author added successfully!")

def display_books(session):
    clear_screen()
    print("List of Books")
    print("==============")
    books = session.query(Book).all()
    if not books:
        print("No books available.")
    else:
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")

