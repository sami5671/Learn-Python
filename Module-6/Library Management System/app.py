import add_book

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
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        add_book.add_books()
        pass
    elif menu == "2":

        pass
    elif menu == "3":

        pass
    elif menu == "4":

        pass
    else:
        print("Choose a valid number")
