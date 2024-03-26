# encrypts a message using a specific encryption key
def encrypt_message(message, encryption_key):
    chars = list(message)
    encrypted_msg = ""
    for char in chars:
        encrypted_char = ""
        if encryption_key > 94:
            encryption_key = encryption_key % 94
        encoded_unicode = ord(char)
        if encoded_unicode + encryption_key > 126:
            new_unicode = encoded_unicode + encryption_key - 126 + 32 - 1
            encrypted_char = chr(new_unicode)
        else:
            encrypted_char = chr(encoded_unicode + encryption_key)
        encrypted_msg = encrypted_msg + encrypted_char
    return encrypted_msg


# decrypts a message that was encrypted with a specific encryption key
def decrypt_message(encrypted_message, encryption_key):
    chars = list(encrypted_message)
    decrypted_msg = ""
    for char in chars:
        decrypted_char = ""
        if encryption_key > 94:
            encryption_key = encryption_key % 94
        encoded_unicode = ord(char)
        if encoded_unicode - encryption_key < 32:
            new_unicode = encoded_unicode - encryption_key + 126 - 32 + 1
            decrypted_char = chr(new_unicode)
        else:
            decrypted_char = chr(encoded_unicode - encryption_key)
        decrypted_msg = decrypted_msg + decrypted_char
    return decrypted_msg


# MAIN PROGRAM
print("Would you like to:\n(1) Encrypt a message\n(2) Decrypt a message")
choice = int(input("Enter option: "))
if choice == 1:
    user_message = input("Enter a message to encrypt: ")
    key = int(input("Enter an encryption key: "))
    encrypted_message = encrypt_message(user_message, key)
    print("Your encrypted message is: " + encrypted_message)
elif choice == 2:
    user_message = input("Enter a message to decrypt: ")
    key = int(input("Enter the decryption key (same as encryption key): "))
    decrypted_message = decrypt_message(user_message, key)
    print("The decrypted (original) message is: " + decrypted_message)
