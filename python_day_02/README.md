```markdown
# Day 02: Caesar Pipeline - Encrypting and Decrypting Messages

Welcome to **Day 02** of my 100 Days of Python Challenge! 🎉 This project focuses on creating a Caesar Cipher Pipeline to encrypt and decrypt messages using a simple shift cipher.

---

## Project Overview

The **Caesar Cipher Pipeline** allows users to:
1. Encrypt a message with a specified shift value.
2. Decrypt a previously encrypted message using the same shift value.

The project is implemented in Python with two primary files:
- **`run_pipeline.py`**: The main program to run the Caesar Cipher Pipeline.
- **`intro.py`**: A module containing ASCII art used to display a welcoming message.

---

## Features

### 1. Encryption
- Converts plaintext to ciphertext by shifting each letter by a specified value.
- Maintains the case of the letters and leaves non-alphabetical characters unchanged.

### 2. Decryption
- Reverses the encryption process by shifting letters back to their original positions.
- Requires the same shift value used during encryption.

---

## Installation and Setup

1. Clone this repository or download the files:
   ```bash
   git clone <[repository-url](https://github.com/michaelxxf/100-days-python-challenge/new/main/python_day_02)>
   ```
2. Ensure you have Python 3.x installed on your system.
3. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

---

## Usage

To run the Caesar Pipeline:
1. Execute the `run_pipeline.py` file:
   ```bash
   python run_pipeline.py
   ```
2. Follow the on-screen prompts:
   - Choose `1` to encrypt a message.
   - Choose `2` to decrypt a message.

### Example

#### Encryption
```plaintext
Welcome to CAESAR PIPELINE
Choose your option 1 or 2...
1). Encrypt message
2). Decrypt message 
==>  1
Enter text to encrypt: hello
Enter shift value (0-25): 3
Encrypted Text: khoor
```

#### Decryption
```plaintext
Welcome to CAESAR PIPELINE
Choose your option 1 or 2...
1). Encrypt message
2). Decrypt message 
==>  2
Enter text to decrypt: khoor
Enter shift value (0 - 25) *should be the same as the encrypt shift value: 3
Decrypted text: hello
```

---

## File Structure

```plaintext
.
├── intro.py           # Contains ASCII art for the welcome message.
├── run_pipeline.py    # The main program to run the Caesar Pipeline.
```

---

## Contributions

Feel free to fork this repository, suggest improvements, or report issues. All feedback is welcome!

---

## Acknowledgments

This project is part of my journey through the **100 Days of Python Challenge**. Special thanks to the Python community for inspiration and support.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
