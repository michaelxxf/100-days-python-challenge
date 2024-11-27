```markdown
# Day 02: URL Shortener

Welcome to **Day 02** of my 100 Days of Python Challenge! 🎉 This project is a **URL Shortener** application built using Python. It provides a graphical user interface (GUI) for shortening URLs effortlessly using the `pyshorteners` library.

---

## Project Overview

The **URL Shortener** application allows users to:
1. Enter a long URL.
2. Shorten the URL with a single click.
3. View the shortened URL directly in the application.

The graphical interface is built using the `customtkinter` library, offering a modern and customizable look.

---

## Features

- **User-Friendly GUI**: Built with `customtkinter` for a clean, responsive, and dark-themed interface.
- **Efficient URL Shortening**: Utilizes the `pyshorteners` library to convert long URLs into shorter, shareable links.
- **Error Handling**: Displays error messages for invalid URLs or unexpected issues during the shortening process.

---

## Installation and Setup

### Prerequisites
1. Python 3.x installed on your system.
2. Required libraries: `customtkinter`, `pyshorteners`.

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required dependencies:
   ```bash
   pip install customtkinter pyshorteners
   ```

---

## Usage

1. Run the application:
   ```bash
   python main.py
   ```


2. Enter the long URL in the input box.

3. Click the **Shorten URL** button.

4. The shortened URL will be displayed in the application, and it will also be printed in the terminal.

---

## File Structure

```plaintext
.
├── main.py         # The main script for the URL Shortener application.
```

---

## Libraries and Modules Used

1. **[customtkinter](https://github.com/TomSchimansky/CustomTkinter)**:
   - A modern and customizable version of the standard `tkinter` library for building user interfaces.
   - Used for creating the GUI components with a sleek, dark-themed appearance.

2. **[pyshorteners](https://pypi.org/project/pyshorteners/)**:
   - A Python library for interacting with URL shortening services.
   - Used to shorten URLs via the `tinyurl` service in this project.

---

## Example Workflow

### Input
```plaintext
Enter URL to shorten: https://example.com/some/long/url
```

### Output
```plaintext
Shortened URL: https://tinyurl.com/xyz123
```

---

## Contributions

Feel free to fork this repository, suggest improvements, or report issues. Contributions are welcome!

---

## Acknowledgments

This project is part of my journey through the **100 Days of Python Challenge**. Big thanks to the Python community for inspiring projects like this one!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
