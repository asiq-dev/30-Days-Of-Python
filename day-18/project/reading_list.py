# The task for this project is relatively simple. We need to update the implementation of our reading list application so that our data is stored in a new file called books.json. We'll be retrieving all of our book data from this new file as well.

import json


# function for adding books
def add_book():
    books = get_all_books()
    title = input("Enter book title name: ").strip().title()
    author = input("Enter book author name: ").strip().title()
    year = input("Year of publication: ").strip()

    books.append({
        "title" : title,
        "author" : author,
        "year" : year,
        "read" : "Not Read"
    })

    with open("books.json", "w") as reading_list:
        json.dump(books,reading_list)

# function for create books.json file
def create_book_file():
    try:
        with open("books.json",'x') as reading_list:
            json.dump([],reading_list)
    except FileExistsError:
        pass

# function for delete books
def delete_book(books, books_to_delete):
    books.remove(books_to_delete)



# function for get all books
def get_all_books():
    
    with open("books.json", "r") as reading_list:
        return json.load(reading_list)
    

# function for find books
def find_books():
    reading_list = get_all_books()
    matching_books = []

    search_term = input("Enter a book title for search: ").strip().lower()

    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)

    return matching_books


# function for mark as read books
def mark_book_as_read(books, books_to_update):
    index = books.index(books_to_update)
    books[index]['read'] = "Read"



# function for update books
def update_reading_list(operation):
    books = get_all_books()
    matching_books = find_books()
    if matching_books:
        operation(books, matching_books[0])

        with open("books.json","w") as reading_list:
            json.dump(books,reading_list)
    else:
        print("Sorry! we didn't find any books matching this title")
    

# function for show books
def show_books(books):
    print()

    for book in books:
        print("{title} by {author} ({year}) - {read}".format(**book))
    
    print()

# call function for create json file
create_book_file()

menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'd' to delete a book
- 'l' to list the books
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

selected_option = input(menu_prompt).strip().lower()


while selected_option != "q":
    if selected_option == "a":
        add_book()
    elif selected_option == "d":
        update_reading_list(delete_book)
    elif selected_option == "l":
        # Retrieves the whole reading list for printing
        reading_list = get_all_books()
        # Check that reading_list contains at least one book
        if reading_list:
            show_books(reading_list)
        else:
            print("your reading is empty!")
    elif selected_option == "r":
        update_reading_list(mark_book_as_read)
    elif selected_option == "s":
        matching_books = find_books()

        if matching_books:
            show_books(matching_books)
        else:
            print("Sorry didn't find any books for that search term")
    else:
        print(f"Sorry, {selected_option} is valid optins!")

    selected_option = input(menu_prompt).strip().lower()