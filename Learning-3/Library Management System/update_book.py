from view_all_books import view_all_books
from save_all_books import save_all_books

def update_a_book(all_books):
    if all_books != []:
        view_all_books(all_books)
        User_ISBN = input("\nEnter the ISBN number of your Book for Update: ")
        flag = False;

        for book in all_books:
            if str(book["isbn"]) == User_ISBN:
                flag = True

                title = input(f"Enter new Title (leave empty to keep '{book['title']}'): ") or book['title']
                author = input(f"Enter new Author (leave empty to keep '{book['author']}'): ") or book['author']
                price = input(f"Enter new Price (leave empty to keep '{book['price']}'): ") or book['price']
                year = input(f"Enter new Year (leave empty to keep '{book['year']}'): ") or book['year']
                quantity = input(f"Enter new Quantity (leave empty to keep '{book['quantity']}'): ") or book['quantity']

                # update book
                book["title"] = title
                book["author"] = author
                book["price"] = float(price)
                book["year"] = int(year)
                book["quantity"] = int(quantity)

                print("\nBook updated successfully!")
                break

        if flag == False:
            print("\nBook not found in the library\n")                

        save_all_books(all_books)

    else:
        print("\nNo books in the library\n")
        return all_books

