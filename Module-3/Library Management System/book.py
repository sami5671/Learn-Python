import add_books 
import view_all_books

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add a book")
    print("2. View all books")

    menu = input("Enter any number: ")

    if menu == "0": 
        print("Thanks for Using Our Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    else: 
        print("Invalid option. Please try again.")
