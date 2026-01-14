# check how strong password is (weak, medium, strong) based meeting following criteria:
# - 8 characters or greater
# - at least 1 number
# - mix of upper and lowercase letters
while True:
    result = 0
    password = input("Enter your password: ")
    # Check for length
    if len(password) >= 8:
        result += 1

 # Check for number
    for character in password:
        if character.isdigit():
            result += 1
            break

    # Check for upper and lowercase letters
    lower = False
    upper = False
    for character in password:
        if character.isalpha() and character.islower():
            lower = True
        if character.isalpha() and character.isupper():
            upper = True
        if lower == True and upper == True:
            result += 1
            break

