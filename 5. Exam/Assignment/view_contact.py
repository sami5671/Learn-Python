import os
import csv

def view_contact():
    if not os.path.exists("All_Contacts.csv"):
        print("No contacts found")
        return False
    else:
        with open("All_Contacts.csv", "r") as file:
            csvFile = csv.reader(file)

            # for organizing my printing data note:-->  (:<{width}) it will format my printing data
            headers = ["Name", "Email", "Phone", "Address"]
            column_widths = [20, 45, 20, 35]  
            header_row = f"{headers[0]:<{column_widths[0]}} {headers[1]:<{column_widths[1]}} {headers[2]:<{column_widths[2]}} {headers[3]:<{column_widths[3]}}"
            print("=" * len(header_row))
            print(header_row)
            print("=" * len(header_row))
            # for organizing my printing data

            for lines in csvFile:
                print(f"{lines[0]:<{column_widths[0]}} {lines[1]:<{column_widths[1]}} {lines[2]:<{column_widths[2]}} {lines[3]:<{column_widths[3]}}")

            return True
