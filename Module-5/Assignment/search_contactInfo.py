from read_contact import read_contact
import csv
def search_contact():
    print("\n============ Search a Contact Info =========\n")
    phone = input("Enter Phone Number: ")
    
    if not read_contact(phone):
        print("Phone number not found")
    else:
        with open("All_Contacts.csv", "r") as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line[2] == phone:
                    print(f"Name: {line[0]}, Email: {line[1]}, Phone: {line[2]}, Address: {line[3]}")
                    break
                