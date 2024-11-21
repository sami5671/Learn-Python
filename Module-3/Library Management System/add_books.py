from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter the Book Title: ")
    author = input("Enter the Author Name: ")
    isbn = int(input("Enter the ISBN: "))
    price = int(input("Enter the Book Price: "))
    year = int(input("Enter the publishing Year: "))
    quantity = int(input("Enter the quantity: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "price": price,
        "year": year,
        "quantity": quantity
    }
    
    all_books.append(book)
    save_all_books(all_books)

    print("Book added successfully.")

    return all_books