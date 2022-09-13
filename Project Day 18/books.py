import json

menu = """Please enter the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

def add_book():
    books = get_all_books()

    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": "Not read"
    })

    with open("./Project Day 18/books.json", "w") as reading_list:
        json.dump(books, reading_list)

def create_book_file():
    try:
        with open("./Project Day 18/books.json", "x") as reading_list:
            json.dump([], reading_list)
    except FileExistsError:
        pass

def delete_book(books, book_to_delete):
    books.remove(book_to_delete)

# Helper function for retrieving data from the csv file
def get_all_books():
    with open("./Project Day 18/books.json", "r") as reading_list:
        return json.load(reading_list)

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Please enter a book title: ").strip().lower()

    # Compares the search term with the title of the book, both in lowercase and appends when same
    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books

def mark_book_as_read(books, book_to_update):
    index = books.index(book_to_update)
    books[index]['read'] = "Read"

def show_books(books):
    print()
    
    for book in books:
        print("{title}, by {author} ({year}) - {read}".format(**book))

    print()

def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open("./Project Day 18/books.json", "w") as reading_list:
            json.dump(books, reading_list)
    else:
        print("Sorry, we didn't find any books matching that title.")

create_book_file()

while True:
    selection = input(menu).strip().lower()

    if selection == "q":
        break
    # Add a new book
    elif selection == "a":
        add_book()
    elif selection == "d":
        update_reading_list(delete_book)
    elif selection == "l":
        # Retrieves the whole reading list for printing
        reading_list = get_all_books()

        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("Your reading list is empty.")
    elif selection == "r":
        update_reading_list(mark_book_as_read)
    elif selection == "s":
        matching_books = find_books()

        # Checks that the search returned at least one book
        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry, we didn't find any books for that search term")
    else:
        print(f"Sorry, '{selection}' isn't a valid option.")

    print()