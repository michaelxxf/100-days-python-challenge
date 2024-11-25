---

### **Caesar Cipher Encryptor**  
A simple Python program that encrypts text using the classic Caesar Cipher algorithm. This project is part of my **100 Days of Code Challenge**.

---

#### **Features**  
- Encrypts any string using a Caesar Cipher.  
- Handles both uppercase and lowercase letters.  
- Preserves non-alphabetic characters (spaces, punctuation, etc.).  
- Allows customizable shift values (0-25).

---

#### **How It Works**  
The Caesar Cipher shifts each letter in the input text by a specified number of positions in the alphabet. For example:
- Input: `Hello, World!`
- Shift: `3`
- Output: `Khoor, Zruog!`
  
- Input: `Hello, world!`
- Shift: `6`
- Output: `Nkrru cuxrj!`

---
#### **Python Functions Used**
- **`chr()`**: Converts a Unicode code point into a character.  
  [Documentation](https://docs.python.org/3/library/functions.html#chr)  
- **`ord()`**: Converts a character into its Unicode code point.  
  [Documentation](https://docs.python.org/3/library/functions.html#ord)

These functions are essential for shifting characters while maintaining their case.

---
#### **Usage**  
1. Run the program:
   ```bash
   python caesar_cipher_encryptor.py
   ```
2. Enter the text to encrypt.  
3. Enter the shift value (between 0 and 25).  
4. The program will output the encrypted text.

---

#### **Example Input/Output**  
```plaintext
Enter text to encrypt: Hello, World!
Enter shift value (0-25): 3
Encrypted Text: Khoor, Zruog!
```

---
#### **References**  
- [chr() Function Documentation](https://docs.python.org/3/library/functions.html#chr)  
- [ord() Function Documentation](https://docs.python.org/3/library/functions.html#ord)  
- [Caesar Cipher Explanation](https://en.wikipedia.org/wiki/Caesar_cipher)

---

#### **License**  
This project is licensed under the [MIT License](LICENSE).

---

#### **Future Improvements**  
- Add decryption functionality. 

---
`https://github.com/michaelxxf/100-days-python-challenge`
