# Password Manager

## Description
- Implementation of the Password Manager App using latest technologies of <strong>Tkinter GUI Framework, OOP concepts, Python, Pyperclip, and JSON Modules</strong>.
- The app saves user's entered username and password to the local file called `data.json` using <strong>json module</strong>; it will create a new file if it does not exist.
- User can generate random password by pressing `Generate Password` button: it generates random password using <strong>random module</strong> and automatically copies new password to clipboard using <strong>pyperclip module</strong>.
- User can search and browse their username and password by entering <strong>Website</strong> name and pressing button `Search`.
- Username field has default email which can be changed using global variable <strong>DEFAULT_USERNAME</strong> in `main.py`.
- The Entry fields cannot be empty: Warning Message will be displayed.
- Exception Handlers are implemented to ensure file and credentials existence.

## How to Setup the Project
1. Create an empty folder
2. Add the folder to workplace area in your VS Code and open terminal OR navigate to the created folder using terminal
3. Download the project .zip file OR Enter to the terminal:
   `git clone https://github.com/ZhenyaChan/password_manager.git`
4. Run the code by entering `python -u "./main.py`