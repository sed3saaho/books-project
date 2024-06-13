##Books Library
Books Library is a simple command-line application for managing books and authors. It allows users to perform various operations such as adding new books, adding new authors, listing books and authors, searching for books, and deleting books or authors from the library.

## Features
1. Add a New Book: Add a new book to the library by providing the title of the book and the name of the author.
2. Add a New Author: Add a new author to the library by providing their name.
3. List of Books: Display a list of all the books available in the library along with their authors.
4. List of Authors: Display a list of all the authors available in the library.
5. Search Books: Search for books by title or author name.
6. Delete Book: Delete a book from the library by providing its title.
7. Delete Author: Delete an author from the library by providing their name.

# Requirements
Python 3.x
SQLAlchemy

# Installation
1. Clone the repository:
git clone <repository_url>

2. Install the dependencies:
pip install -r requirements.txt


# Database Models
## Author
1. Fields:
. id (Integer): Primary key of the author.
. name (String): Name of the author.
2. Relationships:
books (OneToMany): Relationship with the Book model.

## Book
1. Fields:
. id (Integer): Primary key of the book.
. title (String): Title of the book.
. author_id (Integer): Foreign key referencing the id of the author.

## Relationships:
author (ManyToOne): Relationship with the Author model.

# Usage
Navigate to the project directory.
Run the main.py file:

python main.py

Follow the on-screen instructions to perform various operations.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or create a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

