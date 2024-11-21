def view_all_books(all_books):
    if all_books != []:
        for index, book in enumerate(all_books, start = 1) :
            print(f"{index}. Title: {book["title"]} || Author: {book["author"]} || ISBN: {book["isbn"]} || Price: {book["price"]} || Year: {book["year"]} || Quantity: {book["quantity"]}")
    else:
        print("No books available.")
