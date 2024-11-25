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

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value (0-25): "))
    encrypted = caesar_cipher_encrypt(text, shift)
    print("Encrypted Text:", encrypted)
