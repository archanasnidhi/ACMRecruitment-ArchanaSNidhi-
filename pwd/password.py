import re
def validate_password(password):
    if len(password) !=8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~-]', password):
        return False
    first=password[0]
    if re.match(r'^[\d!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~-]', first):
        return False
    if password in [ "A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]:
        return False
    return True

password = input("Enter your password: ")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
