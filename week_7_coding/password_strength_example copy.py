def password_strength(password):
    ''' This program checks the user's input password
    and categorizes it as weak, medium, or strong. '''

    # Check for password length
    length = len(password)
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)

    # Determine strength
    if length < 6:
        strength = 'weak'
    elif length < 10:
        if has_letter and has_number:
            strength = 'medium'
        else:
            strength = 'weak'
    else:  # length 10 or more
        if has_letter and has_number:
            strength = 'strong'
        else:
            strength = 'medium'

    return strength

# Example usage
user_password = input("Enter your password: ")
print(f"Password strength: {password_strength(user_password)}")



