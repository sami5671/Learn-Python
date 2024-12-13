import json
import os

from response_messages import no_book_found, remove_book
from view_books import view_books


def delete_book():
    if not os.path.exists("all_books.json"):
        no_book_found()
        return False
    else:
        view_books()
        with open("all_books.json", "r") as file:
            books = json.load(file)

        title = input("Enter the title of the book to delete: ")

        found = False
        for index, book in enumerate(books):
            if book["title"] == title:
                found = True
                del books[index]
                break

        if found:
            with open("all_books.json", "w") as file:
                json.dump(books, file, indent=4)
                remove_book()
        else:
            no_book_found()
            return False
