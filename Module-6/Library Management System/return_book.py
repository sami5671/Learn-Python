import json
import os


def return_book():
    # borrow_book = []

    if not os.path.exists("borrow_books.json"):
        print("No book borrowed.")
        return False

    with open("borrow_books.json", "r") as file:
        borrow_book = json.load(file)
        title = input("Enter the book Title You want to return: ")

        found = False
        for index, book in enumerate(borrow_book):
            if book["book_title"] == title:
                found = True
                del borrow_book[index]
                break

        if found:
            with open("borrow_books.json", "w") as file:
                json.dump(borrow_book, file, indent=4)

            with open("all_books.json", "r") as file:
                books = json.load(file)
                for book in books:
                    if book["title"] == title:
                        book["quantity"] += 1
                        break
            with open("all_books.json", "w") as file:
                json.dump(books, file, indent=4)
                print("Book returned successfully.")

            return True
        else:
            print("No such book borrowed.")
            return False
