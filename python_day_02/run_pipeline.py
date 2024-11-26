from intro import art
def caesar_cipher_encrypt(s, shift):
    result = ""
    for char in s:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_cipher_decrypt(v, shift):
    result = ""
    for char in v:
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    return result 



if __name__ == "__main__":
    welcome_msg = int(input("""Welcome to CAESAR PIPELINE
                            Choose your option 1 or 2...
                            1). Encrypt message
                            2). Decrypt message \n ==>  """))

    if welcome_msg == 1:    
        text = input("Enter text to encrypt:    ")
        shift = int(input("Enter shift value (0-25): "))
        encrypted = caesar_cipher_encrypt(text, shift)
        print("Encrypted Text:", encrypted)

    elif welcome_msg == 2:
        text = input("Enter text to decrypt:    ")
        shift = int(input("Enter shift value (0 - 25) *should be the same as the encrypt shift value:   "))
        decrypted = caesar_cipher_decrypt(text, shift)
        print("Decrypted text:  ", decrypted)
    else:
        print("Wrong input")
