def add_book():
    title = input("Enter book title name: ").strip().title()
    author = input("Enter book author name: ").strip().title()
    year = input("Year of publication: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title},{author},{year}\n")

# Helper function for retrieving data from the csv file
def get_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year = book.strip().split(",") # Extracts the values from the CSV data

# Creates a dictionary from the csv data and adds it to the books list
            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books
    

def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Enter a book title for search: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books


def show_books(books):
    print()

    for book in books:
        print(f"{book['title']}, by {book['author']} ({book['year']})")






menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()


while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        # Retrieves the whole reading list for printing
        reading_list = get_all_books()
        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("your reading is empty!")
    elif selected_option == "s":
        matching_books = find_books()

        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry didn't find any books for that search term")
    else:
        print(f"Sorry, {selected_option} is valid optins!")

    selected_option = input(menu_prompt).strip().lower()