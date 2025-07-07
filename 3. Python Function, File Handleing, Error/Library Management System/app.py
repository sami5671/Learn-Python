import add_book 
import view_all_books
import update_book
import delete_book

all_books = []

while True:
    print("\n=================== Welcome to Library Management System ==================\n")
    print("0. Exit")
    print("1. Add a book")
    print("2. View all books")
    print("3. Update a book")
    print("4. Delete a book")

    menu = input("\nSelect a number What do you want to do: ")

    if menu == "0": 
        print("\n============Thanks for Using Our Library Management System==========\n")
        break
    elif menu == "1":
        print("\n============Please Give Info About the book=========\n")
        all_books = add_book.add_books(all_books)
    elif menu == "2":
        print("\n============Here are All Books=========\n")
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        print("\n============Update a Book=========\n")
        update_book.update_a_book(all_books)
    elif menu == "4":
        print("\n============Delete a Book=========\n")
        delete_book.delete_a_book(all_books)
    else: 
        print("Invalid option. Please try again.")
