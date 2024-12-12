import add_book
import delete_book
import update_book
import view_books
from response_messages import style_CLI

while True:
    print(
        "\n========================Welcome to Library Management System==============================="
    )
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Delete Book")

    menu = input("Please select an option: ")

    if menu == "0":
        style_CLI("Thanks for using Library Management System")
        break
    elif menu == "1":
        style_CLI("Please add Your Book to Library Management System")
        add_book.add_books()
    elif menu == "2":
        view_books.view_books()
    elif menu == "3":
        update_book.update_book()
    elif menu == "4":
        delete_book.delete_book()
    else:
        print("Choose a valid number")
