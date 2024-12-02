import add_contact

while True:
    print("\n=================== Welcome to Contact Book Management System ==================\n")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Remove Contacts")
    print("4. Search Contacts")
    
    menu = input("\nSelect a number What do you want to do: ")

    if menu == "0": 
        print("\n============ Thanks for Using Contact Book Management System ==========\n")
        break
    elif menu == "1":
        print("\n============ TO Add Contact Give the Info =========\n")
        add_contact.add_contact()
    elif menu == "2":
        print("\n============ Here Are The All Contact List =========\n")
        # print(withdraw(ostad, money))
    elif menu == "3":
        print("\n============ Remove a Contact Info =========\n")
        # print(get_balance(ostad))
    elif menu == "4":
        print("\n============ Search a Contact Info =========\n")
        
        # print(get_balance(ostad))
    else: 
        print("Invalid option. Please try again.")