import json
import os
from datetime import datetime

import save_book
from response_messages import no_book_found, update_book_success
from view_books import view_books


def update_book():

    if os.path.exists("all_books.json"):
        view_books()
        flag = False
        with open("all_books.json", "r") as file:
            books = json.load(file)
            search_book = input("Enter the book name that you want to update: ")
            for book in books:
                if book["title"] == search_book:

                    title = input("Enter Book Title: ")
                    author = input("Enter Author Name: ")
                    year = int(input("Enter Publishing Year Number: "))
                    price = input("Enter Book Price: ")
                    quantity = int(input("Enter Quantity Number: "))

                    book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                    book["title"] = title
                    book["author"] = author
                    book["year"] = year
                    book["price"] = price
                    book["quantity"] = quantity
                    book["bookLastUpdatedAt"] = book_last_updated_at

                    flag = True
                    break

            if flag:
                with open("all_books.json", "w") as file:
                    json.dump(books, file, indent=4)
                    update_book_success()
    else:
        no_book_found()
        return False
