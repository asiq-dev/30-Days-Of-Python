# Problem:
# The brief
# For this project the application needs to have the following functionality:

# 1. Users should be able to add a book to their reading list by providing a book title, an author's name, and a year of publication.
# 2. The program should store information about all of these books in a Python list.
# 3. Users should be able to display all the books in their reading list, and these books should be printed out in a user-friendly format.
# 4. Users should be able to select these options from a text menu, and they should be able to perform multiple operations without restarting 
#    the program. You can see an example of a working menu in the post on while loops






# Solutions:


reading_list = []
menu_prompt = """Please enter one of the following options:

-'a' to add a book
-'l' to displaying list of the books
-'q' to quite the prorgamm

what would you like to do? """

selected_options = input(menu_prompt).strip().lower()

#adding book function
def add_book():
    title = input("Enter book tile: ").strip().title()
    author = input("Enter book author name: ").strip().title()
    year = input("Enter publication year : ").strip()
    
    reading_list.append({
        "title" : title,
        "author" : author,
        "year" : year
    })
    print("book list add successfully ")


#showig book function
def show_book():
    print()
    for book in reading_list:
        title, author, year = book.values()
        print(f"{title}, by {author} ({year})")
    print()


# main function
while selected_options != 'q':
    if selected_options == 'a':
        add_book()
    elif selected_options == 'l':
        if reading_list:
            show_book()
        else:
            print("Book list is empty!")
    else:
        print(f"Sorry,{selected_options} is invalid options! ")
    
    selected_options = input(menu_prompt).strip().lower()



