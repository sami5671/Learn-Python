from save_contactInfo import save_contact
import csv
import os

def add_contact():
    name = input("Enter the Name: ")
    email = input("Enter the email: ")
    phone = int(input("Enter the Phone Number: "))
    address = input("Enter the Address: ")

    contactInfo = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }
           
    # check if the phone number is already exist or not
    if not os.path.exists("All_Contacts.csv"):
        with open("All_Contacts.csv", "w") as file:
            save_contact(contactInfo)
        return False
    
    
    with open("All_Contacts.csv", "r") as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            if phone == int(lines[2]):
                print("Phone number already exist")
                return True

        save_contact(contactInfo)
        return False