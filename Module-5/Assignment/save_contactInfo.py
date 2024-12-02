
def save_contact(contactInfo):
    with open("All_Contacts.csv", "a") as fp:
            info = f"{contactInfo['name']}, {contactInfo['email']}, {contactInfo['phone']}, {contactInfo['address']},\n"
            fp.write(info)
            print("Contact Information added successfully")