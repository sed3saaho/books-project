# utils.py

import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_input(prompt, validator):
    """
    Prompts the user for input using the provided prompt message and validates the input
    using the provided validator function.
    """
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def paginate(items, page_size=10):
    """
    Paginates a list of items with the specified page size and prompts the user for
    the page number to display.
    """
    total_pages = (len(items) + page_size - 1) // page_size
    for page_num in range(total_pages):
        start_idx = page_num * page_size
        end_idx = min(start_idx + page_size, len(items))
        page_items = items[start_idx:end_idx]
        print(f"Page {page_num + 1}/{total_pages}:")
        for item in page_items:
            print(item)
        input("Press Enter to continue...")
