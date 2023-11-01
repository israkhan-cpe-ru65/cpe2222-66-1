ALPHABEL_CHAR_UPPERCASE_OFFSET = 64
ALPHABEL_CHAR_LOWERCASE_OFFSET = 96

def main():
    plain_text = handle_plain_text_input()
    secret_key = handle_secret_key_input()
    
    cypher_text = encrypt(plain_text, secret_key)
    print("The encrypted ciphertext:", cypher_text)

    decrypted_text = decrypt(cypher_text, secret_key)
    print("The decryption results:", decrypted_text)

    return


def handle_plain_text_input():
    plain_text = input("Enter your plaintext (Alphabet Only):")
    
    if not plain_text.isalpha():
        print("Please enter alphabet only")
        return handle_plain_text_input()
    
    return plain_text


def handle_secret_key_input():
    secret_key = input("Enter your secret key (Number Only):")
    
    if not secret_key.isdigit():
        print("Please enter number only")
        return handle_secret_key_input()
    
    return int(secret_key)


def encrypt(plain_text, key):
    cipher_text = ""

    for char in plain_text:
        offset = 0
        offset = ALPHABEL_CHAR_LOWERCASE_OFFSET \
                 if char.islower() \
                 else ALPHABEL_CHAR_UPPERCASE_OFFSET
        char_uc = ord(char)

        offset += 1 \
            if char_uc % key == 0 \
            or (char_uc + key - offset) % 26 == 0 \
            else 0

        encrypted_char = chr(
            (char_uc + key - offset) % 26 + offset)
        cipher_text += encrypted_char

    return cipher_text


def decrypt(cipher_text, key):
    plain_text = ""

    for char in cipher_text:
        offset = ALPHABEL_CHAR_LOWERCASE_OFFSET \
                 if char.islower() \
                 else ALPHABEL_CHAR_UPPERCASE_OFFSET
        char_uc = ord(char)

        offset += 1 \
            if char_uc % key == 0 \
            or (char_uc - key - offset) % 26 == 0 \
            else 0
            
        decrypted_char = chr(
            ((char_uc - key - offset) % 26) + offset)
        plain_text += decrypted_char
        
    return plain_text


if __name__ == "__main__":
    main()
