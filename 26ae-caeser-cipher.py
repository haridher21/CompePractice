def caesarCipherEncryptor(string, key):
    ASCII_A, L_ALPHABETS, new_string = ord('a'), 26, ""
    for i in range(len(string)):
        new_string += chr(((((ord(string[i]) - ASCII_A) % L_ALPHABETS) + key) % L_ALPHABETS) + ASCII_A)
    return new_string
