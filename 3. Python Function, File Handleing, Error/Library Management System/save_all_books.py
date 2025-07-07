def save_all_books(all_books):
    with open("All_Books.csv", "w") as fp:
        for book in all_books:
            line = f"{book["title"]}, {book["author"]},{book["isbn"]},{book["price"]},{book["year"]},{book["quantity"]},\n"
            fp.write(line)
