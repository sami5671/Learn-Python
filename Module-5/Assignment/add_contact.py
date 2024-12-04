from save_contactInfo import save_contact
import csv
import os
from input_validation import check_email_validation, check_phone_validation, check_name_validation

def add_contact():
    name = input("Enter the Name: ")
    if not check_name_validation(name):
        print("Name should be string")
        return False
    
    email = input("Enter the email: ")
    if not check_email_validation(email):
        print("Invalid email format")
        return False
    
    phone = int(input("Enter the Phone Number: "))
    if not check_phone_validation(phone):
        print("Phone number should be 11 digit and integer")
        return False
        
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