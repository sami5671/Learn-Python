def check_name_validation(name):
    if not all(name.isalpha() or name.isspace() or name == "." for name in name):
        return False
    return True
