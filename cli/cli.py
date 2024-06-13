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

def display_authors(session):
    clear_screen()
    print("List of Authors")
    print("================")
    authors = session.query(Author).all()
    if not authors:
        print("No authors available.")
    else:
        for author in authors:
            print(f"Name: {author.name}")

def search_books(session):
    clear_screen()
    print("Search Books")
    print("============")
    search_term = input("Enter title or author name to search: ")
    books = session.query(Book).filter(Book.title.ilike(f"%{search_term}%") |
                                       Book.author.has(name=search_term)).all()
    if not books:
        print("No books found.")
    else:
        print("Matching Books:")
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")

def delete_book(session):
    clear_screen()
    print("Delete Book")
    print("===========")
    title = input("Enter the title of the book to delete: ")
    book = session.query(Book).filter_by(title=title).first()
    if not book:
        print("Book not found.")
    else:
        session.delete(book)
        session.commit()
        print("Book deleted successfully!")

def delete_author(session):
    clear_screen()
    print("Delete Author")
    print("=============")
    name = input("Enter the name of the author to delete: ")
    author = session.query(Author).filter_by(name=name).first()
    if not author:
        print("Author not found.")
    else:
        session.delete(author)
        session.commit()
        print("Author deleted successfully!")

def main():
    with SessionLocal() as session:
        while True:
            clear_screen()
            print("Books Library")
            print("==============")
            print("1. Add a New Book")
            print("2. Add a New Author")
            print("3. List of Books")
            print("4. List of Authors")
            print("5. Search Books")
            print("6. Delete Book")
            print("7. Delete Author")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_book(session)
            elif choice == '2':
                add_author(session)
            elif choice == '3':
                display_books(session)
            elif choice == '4':
                display_authors(session)
            elif choice == '5':
                search_books(session) 
            elif choice == '6':
                delete_book(session)
            elif choice == '7':
                delete_author(session)
            elif choice == '8':
                break
            input("Press Enter to continue...")

if __name__ == '__main__':
    main()