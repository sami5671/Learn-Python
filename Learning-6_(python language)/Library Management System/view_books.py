import json
import os

from response_messages import no_book_found, style_CLI


def view_books():

    if not os.path.exists("all_books.json"):
        no_book_found()
        return False
    else:
        with open("all_books.json", "r") as file:
            all_books = json.load(file)

            if all_books != []:
                style_CLI("All Books")
                for book in all_books:
                    print(
                        f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}"
                    )
                return True
            else:
                no_book_found()
                return False
