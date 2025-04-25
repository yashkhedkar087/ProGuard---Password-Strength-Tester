# ProGuard - Password Strength Tester

## Overview

ProGuard is a Python-based graphical user interface (GUI) tool that helps users test the strength of their passwords and generate secure, random passwords. The app uses simple but effective algorithms to evaluate password strength based on criteria like length, character variety, and complexity. It also offers real-time feedback, security suggestions for weak passwords, and a password generator feature.

## Features

- **Password Strength Tester**: Check password strength based on length, uppercase, lowercase, digits, and special characters.
- **Password Generator**: Generate strong passwords with a customizable length.
- **Password Visibility Toggle**: Show or hide the entered password for convenience.
- **Clipboard Copy**: Copy generated passwords to the clipboard for easy use.
- **Real-Time Suggestions**: Get suggestions for improving weak passwords.

## Requirements

- Python 3.x
- Tkinter (Tkinter is included by default with Python, so no additional installation is needed)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/YashKhedkar/ProGuard.git
    cd ProGuard
    ```

2. Install Python (if not installed) from the official Python website: https://www.python.org/downloads/

3. Run the application:

    ```bash
    python password_strength_tester.py
    ```

## Usage

1. **Enter a Password**: Type your password in the entry box.
2. **Check Strength**: Click the "Check Strength" button to evaluate the password.
   - The strength will be categorized as "Weak", "Moderate", or "Strong".
   - Weak passwords will also get suggestions for improvement.
3. **Generate Password**: Click the "Generate Strong Password" button to create a secure random password.
4. **Toggle Visibility**: Click the "View Password" button to toggle the visibility of your entered password.
5. **Copy Password**: Generated passwords can be copied to your clipboard by clicking the "Copy to Clipboard" button.

## Features Details

### Password Strength Evaluation
The password strength is evaluated based on the following criteria:
- **Length**: The password should be at least 8 characters long. Stronger passwords are longer.
- **Character Variety**: It checks if the password contains:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*(),.?":{}|<>)
  
### Password Generator
The generator creates a password by randomly picking characters from a pool of:
- Uppercase letters
- Lowercase letters
- Digits
- Special characters

The default length is 12 characters, but you can adjust the length using the length slider.

## Screenshots

*Insert screenshots here if desired*

## Future Enhancements

- **Dark/Light Theme Toggle**: Add a toggle to switch between dark and light modes.
- **Strength Meter**: Add a visual progress bar or meter to indicate password strength dynamically.
- **Password History**: Save the history of tested passwords and allow users to view them.
- **Web Version**: Convert this project into a web application using Flask or Django.
- **Export to File**: Export generated passwords or tested passwords to a file for record-keeping.

## License

This project is open-source and available under the MIT License. Feel free to use and modify it for educational purposes.

## Contact

For any queries or contributions, feel free to contact me:

- **Name**: Yash Khedkar
- **GitHub**: https://github.com/YashKhedkar087
- **Email**: yash.khedkar@example.com

---

**Happy Password Protecting!** 🔐
