from view_all_books import view_all_books
from save_all_books import save_all_books

def delete_a_book(all_books):
    if all_books:  
        flag = False
        view_all_books(all_books)
        User_ISBN = input("Enter the ISBN of the book to delete: ")

        for book in all_books:
            if str(book["isbn"]) == User_ISBN:
                flag = True
                all_books.remove(book) 
                print("\nBook deleted successfully!")
                break

        if not flag:
            print("\nBook not found in the library.\n")
        
        save_all_books(all_books)

    else:
        print("\nNo books in the library.\n")
        return all_books
