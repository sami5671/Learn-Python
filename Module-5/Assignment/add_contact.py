from save_contactInfo import save_contact
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

    save_contact(contactInfo)

    return contactInfo