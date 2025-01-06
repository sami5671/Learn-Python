import os
import csv
def search_contact():
    print("\n============ Search a Contact Info =========\n")
    phone = input("Enter Phone Number: ")
    
    if not os.path.exists("All_Contacts.csv"):
        print("The contact list is empty. please create a new contact then search again")
        return False
    else:
        with open("All_Contacts.csv", "r") as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line[2].strip() == phone:
                    print("\n================Contact Found:===================")
                    print("Name: ", line[0])
                    print("Email: ", line[1])
                    print("Phone: ", line[2])
                    print("Address: ", line[3])
                    return True
        print("Phone number not found")
        return False
    
    
                