def check_access(age, is_member, has_permission):
    """
    This function checks if a user has access to a resource based on their age,
    status and permission level
    """

    if age >= 18 and is_member or has_permission: # Logical and - both conditions must be true
        return True
    elif has_permission:
        return True
    elif not is_member and age <= 18:
        return False
    else:
        return False
    
    # Test Cases
print(check_access(20, True, False)) # Output: True
print(check_access(16, False, True)) # Output: True
print(check_access(17, False, False)) # Output: False
print(check_access(22, False, False)) # Output: False