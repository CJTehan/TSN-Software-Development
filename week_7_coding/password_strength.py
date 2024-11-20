def password_strength(password):
    """
    This function will check the strength of the password on nested criteria
    """

    if len(password) < 8:   # Checks length
        return "weak" # Too short
    
    if any(char.isdigit() for char in password):
        if any(char.isalpha() for char in password):
            if any(char in "!@#$%^*" for char in password):
                return "strong"
            else:
                return "medium"
        else:
            return "weak"
        
    else:
        return "weak"



password = input("Enter your password: ")
strength = password_strength(password)
print(f"Password_strength: {strength}")
