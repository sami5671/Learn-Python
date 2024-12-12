def check_name_validation(name):
    if not all(name.isalpha() or name.isspace() or name == "." for name in name ):
        return False
    return True

def check_number(number):
    str_number = str(number)
    if not str_number.isdigit():
        return False
    return True