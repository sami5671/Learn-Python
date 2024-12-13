import json
import os
from datetime import datetime, timedelta

from response_messages import no_book_found, success


def lend_book():
    borrow_books = []
    if not os.path.exists("all_books.json"):
        no_book_found()
        return False

    with open("all_books.json", "r") as file:
        books = json.load(file)

    title = input("Enter the title of the book to lend: ")
    for book in books:
        if book["title"] == title:
            if book["quantity"] > 0:
                borrower_name = input("Enter borrower's name: ")
                borrower_phone = input("Enter borrower's phone number: ")
                return_days = int(input("Enter the number of days to return: "))

                return_due_date = datetime.now() + timedelta(days=return_days)
                return_due_date_str = return_due_date.strftime("%d-%m-%Y %H:%M:%S")

                book["quantity"] = book["quantity"] - 1
                book["bookLastUpdatedAt"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                with open("all_books.json", "w") as file:
                    json.dump(books, file, indent=4)

                borrower_details = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book["title"],
                    "return_due_date": return_due_date_str,
                }

                if not os.path.exists("borrow_books.json"):
                    with open("borrow_books.json", "w") as file:
                        json.dump([borrower_details], file, indent=4)
                else:
                    with open("borrow_books.json", "r") as file:
                        borrow_books = json.load(file)
                        borrow_books.append(borrower_details)

                    with open("borrow_books.json", "w") as file:
                        json.dump(borrow_books, file, indent=4)

                success()
                return True
            else:
                print("There are not enough books available to lend.")
                return False

    print("Book not found.")
    return False
