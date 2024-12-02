import csv 
import os
def read_contact(phone):
    if not os.path.exists("All_Contacts.csv"):
        return False
    else:
        with open("All_Contacts.csv", "r") as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line[2].strip() == phone:
                    return True