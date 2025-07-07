def check_phone_validation(phone):
    phone_str = str(phone)
    if len((phone_str)) != 10 or not phone_str.isdigit():
        return False
    return True

def check_email_validation(email):
    if "@" not in email or "." not in email:
        return False
    return True

def check_name_validation(name):
    if not all(name.isalpha() or name.isspace() or name == "." for name in name ):
        return False
    return True