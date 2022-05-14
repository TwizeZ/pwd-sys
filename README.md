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

The following steps must be completed for the program to run.

1. Install Python 3.7 or newer from the following link:
>Download: https://www.python.org/downloads/

2. Clone repository
```cmd
    git clone https://github.com/twizez/pwd-sys/
```
3. Installera Flask
```cmd
    pip install Flask
```
4. Installera pygame
```cmd
    pip install pygame
```

The following intsallations must be made for the program to run.
