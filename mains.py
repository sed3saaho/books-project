# main.py

from cli.cli import main as CLI  # Adjusted import statement
from orm.database import engine, SessionLocal
from orm.models import Base
from utils import clear_screen
from sample_books import sample_books  # Importing the sample books dataset

def main():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

    # Initialize CLI and database session
    cli = CLI()

    # Run the CLI application
    try:
        cli.run()
    finally:
        # Close the database session when done
        SessionLocal().close()

if __name__ == "__main__":
    main()
