# pwd-sys : Password System

## **Description**

**pwd-sys** is a Password system, made for a CLI-interface.

This program is written in Python, and was created as my final's project in my programming class, PRRPRR01.

The program consists of the following files:

### 1. pwd.py

*Contains all code needed for the program to work as intended.*

### 2. passwords.txt

*This is the database where all entries/users are stored. This file can be manually edited, but it is strongly recommended that you do not touch this.*

Use the built-in features in the program to modify the entries in the database.

### 3. activity.log

*This log file collects all log-messages related to the program.*

> If you do not spot an acitivity.log file in the system folders, the file has not yet been created. Logging in to the system a first time will create the file.

**Logs are captured when:**

1. A user tries to log in
    1. Successful login attempt
    1. Unsuccessful login attempts
1. A user logs out.
1. A user creates a new entry
1. An entry is being modified
    1. Successful modifications
    1. Unsuccessful modifications
1. An entry is being deleted
    1. Successful deletions
    1. Unsuccessful deletions
1. Database is opened.
1. A user is viewing a list of all users in the system.
1. A user is viewing another user's entry in detail.

### 4. README.md

***This is the file you are currently reading.*** Here, you can find information about the program, including changelogs, installation instructions, system requirements, and more.

## Technology

The program's frontend and backend design is written in Python, while Markdown, HTML, and CSS is used for the README-file.

- Python
- Markdown
- HTML
- CSS

## Requirements/Prequesitions

**Following requirements must be fulfilled in order to run this program:**

- Python 3.7+
- Git 2.33.0+
- Getpwd module

## Installation

### The following steps must be completed for the program to run.

For this program to run, you need to install Python version 3.7 or newer from the following link:
>https://www.python.org/downloads/

After that, you will have to complete the following steps in your CLI/terminal:

1. Clone repository
```cmd
    git clone https://github.com/twizez/pwd-sys/
```

2. Installera getpwd
```cmd
    pip install getpwd
```

The following installations must be made for the program to run.

## Code conventions

All code written is following the PEP-8 standard to keep it structured and organized.

Docstrings are also used to comment some more advanced functions.

## Usage

This project is created as a password system in a CLI-interface.

### Menu

A menu with different features is also included in the program. In this menu, you are able to manage the system and its users/entries.

![main menu](resources/menu.png)

As you can see, the menu offers many features and settings for your user.

1. **Create new entry** - Where you can create a brand new user/entry.
2. **List of all entries** - Here, you can view a list of all users currently registered in the system. Only their username is shown in this list.
3. **Search entries** - Type the name of a user, and their entry will be displayed. This view includes their username, e-mail, and notes. Their password will remain hidden.
4. **Log out** - Select this option to be logged out of the system. This will take you back to the log-in screen.
5. **Exit appllication** - This will shut down the system and exit the program. Upon this, the console will be completely cleared.
6. **Change username** - Used to change the currently logged in user's username. You cannot edit other user's credentials.
7. **Change password** - Used to change the currently logged in user's password. You cannot edit other user's credentials.
8. **Delete user** - This action will delete the currently logged in user's entry permanently. Be careful with this.

### Log-in

The log-in screen is simple and intuitive, leaving you with a fast and easy system launch.

Input your username and password to access the system.

![log-in screen](resources/login.PNG)

### Admin

As you set-up and install the system for the first time, you need to use the standard user to get access to the system. You will then be greeted by the screen below.

![admin-login](resources/admin_msg.PNG)

Note that you cannot delete the standard admin user, nor change its username. However, you can edit the password of the entry.

## Example

This is a recorded example of how the program works.

[*Click here to open video*](https://vimeo.com/710155380)

## Roadmap

## Changelog

## Contribution

## License

## Contact

## Acknowledgements

>Add standard details somewhere (admin, admin)
