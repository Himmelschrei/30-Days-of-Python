reading_list = []

menu = """Please enter the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    new_book = {
        "title": title,
        "author": author,
        "year": year
    }

    reading_list.append(new_book)

def show_books():
    for book in reading_list:
        print(f"{book['title']}, by {book['author']} ({book['year']})")


while True:
    selection = input(menu).strip().lower()

    if selection == "q":
        break
    elif selection == "a":
        add_book()
    elif selection == "l":
        if reading_list:
            show_books()
        else:
            print("Reading list is empty. Please enter books in order to fill it out.")
    else:
        print(f"Sorry, '{selection}' isn't a valid option.")
