menu = """Please enter the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    with open("./Project Day 14/books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year},Not Read\n")

def delete_book(books, book_to_delete):
    books.remove(book_to_delete)

# Helper function for retrieving data from the csv file
def get_all_books():
    books = []

    with open("./Project Day 14/books.csv", "r") as reading_list:
        for book in reading_list:
            # Extracts the values of the CSV data
            title, author, year, read = book.strip().split(",")

            # Creates a dictionary from the CSV data and adds it to the books list
            books.append({
                "title": title,
                "author": author,
                "year": year,
                "read": read
            })
    
    return books

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
        print(f"{book['title']}, by {book['author']} ({book['year']}) - {book['read']}")

    print()

def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()

    if matching_books:
        operation(books, matching_books[0])

        with open("./Project Day/books.csv", "w") as reading_list:
            for book in books:
                reading_list.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")
    else:
        print("Sorry, we didn't find any books matching that title.")

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