print("Please complete the access check")

def check_access(age, status, level):
    if age >= 18:
        print("Access Granted")
    else:
        print("Denied")
    if status == "Member":
        print("Member Recognised")
    else:
        print("User not recognised")
    if level > 2:
        print("You have partial access to the system")
    elif level == 5:
        print("Full Access Permissions granted")
    else:
        print("You are not permitted to access this")

check_access()
