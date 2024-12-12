import os
import random
from datetime import datetime

from input_validation import check_name_validation, check_number
from save_book import save_book


def add_books():
    title = input("Enter Book Title: ")
    if not check_name_validation(title):
        print("The book title should be a valid string")
        return False

    author = input("Enter Author Name: ")
    if not check_name_validation(author):
        print("The book title should be a valid string")
        return False

    year = input("Enter Publishing Year Number: ")
    if not check_number(year):
        print("The year should be a valid number")
        return False

    quantity = input("Enter Book Quantity: ")
    if not check_number(quantity):
        print("The quantity should be a valid number")
        return False

    price = input("Enter Book Price: ")

    isbn = random.randint(1000, 9999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    bookDetails = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": "",
    }

    save_book(bookDetails)
