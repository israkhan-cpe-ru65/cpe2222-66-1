def main():
    password_input = input("Setting your password:")
    
    if (not any(letter.isupper() for letter in password_input)):
        print(
            "!!!ERROR!!! The password must contain at least a capital letter")
    elif (not any(letter.islower() for letter in password_input)):
        print(
            "!!!ERROR!!! The password must contain at least a lowercase letter")
    elif (not any(letter.isdigit() for letter in password_input)):
        print(
            "!!!ERROR!!! The password must contain at least a number")
    elif (len(password_input) < 8):
        print(
            "!!!ERROR!!! The password must contain at least 8 characters")
    elif (len(password_input) > 16):
        print(
            "!!!ERROR!!! The password must not contain more than 16 characters")
    else:
        print(":-) Your password is correct (-:)")

    return


if __name__ == "__main__":
    main()
