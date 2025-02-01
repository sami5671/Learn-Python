import json
import os

from response_messages import add_book_success


def save_book(bookDetails):
    books = []

    if not os.path.exists("all_books.json"):
        with open("all_books.json", "w") as file:
            books.append(bookDetails)
            json.dump(books, file, indent=4)
            add_book_success()
        return True

    with open("all_books.json", "r") as file:
        books = json.load(file)
        books.append(bookDetails)

    with open("all_books.json", "w") as file:
        json.dump(books, file, indent=4)
        add_book_success()
    return True
