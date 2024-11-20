stored_pass = "password"
password = ""
pass_mismatch = stored_pass != password
permitted_guesses = 3
attempts = 0

while attempts < permitted_guesses:
    password = input("Enter your password:")
    pass_mismatch = stored_pass != password
    if stored_pass == password:
        print("Access granted")
        break
    else:
        attempts += 1
        print(f"Incorrect password, you have {permitted_guesses - attempts} left")
        continue
if attempts == permitted_guesses:
    print("Access Denied, you have no guesses remaining")
