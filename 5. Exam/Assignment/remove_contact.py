import os
import csv
from view_contact import view_contact

def remove_contact():
    if not os.path.exists("All_Contacts.csv"):
        print("No contacts found.")
        return False
    else:
        view_contact()  
        
        phone = input("\nEnter the phone number of the contact to remove: ")

        with open("All_Contacts.csv", "r") as main_csvFile, open("temp_contacts.csv", "w", newline="") as temp_csvFile:
            file_reader = csv.reader(main_csvFile)  
            file_writer = csv.writer(temp_csvFile)  
            
            phone_number_match = False
            
            for line in file_reader:
                
                if line[2].strip() == phone:
                    phone_number_match = True
                    continue  
                
                file_writer.writerow(line) 
        
        if phone_number_match:
            os.remove("All_Contacts.csv")
            os.rename("temp_contacts.csv", "All_Contacts.csv")
            print(f"\nContact with phone number {phone} has been removed successfully.")
        else:
            os.remove("temp_contacts.csv") 
            print(f"\nNo contact found with the phone number {phone}.")

        return True
