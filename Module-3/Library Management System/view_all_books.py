

def view_all_books(all_books):
    if all_books != []:
        for book in all_books:
            print(f"Title: {book["title"]}, | Author: {book["author"]},| ISBN: {book["isbn"]},| Price: {book["price"]},| Year: {book["year"]},| Quantity: {book["quantity"]}")
    else:
        print("No books available.")
