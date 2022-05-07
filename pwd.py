#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

from time import sleep
from getpwd import getpwd
import os
import logging

logging.basicConfig(filename="activity.log", 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    filemode='a', encoding="utf-8", datefmt='%d-%m-%y %H:%M:%S')
#Let us Create an object 
logger = logging.getLogger()
# Set the threshold of logger to INFO
logger.setLevel(logging.INFO)

def options():
    print()
    print("[1] Create new entry.")
    print("[2] List of all entries.")
    print("[3] Search entries.")
    print("[4] Log out.")
    print("[0] Exit application.")
    print()
    print("You can also use the following inputs to change your user settings:")
    print("Change username - 'usernm'")
    print("Change password - 'passwd'")
    print("Delete user - 'delusr'")

def menu():
    options()
    choice = input(">> ")

    # BUG Does not close application when entering 0, just logs you out.

    while choice != "0":
        if choice == "1":
            createEntry()
        elif choice == "2":
            pwdList()
        elif choice == "3":
            findPwd()
        elif choice == "4":
            break
        elif choice == "usernm":
            pass
        elif choice == "passwd":
            pass
        elif choice == "delusr":
            deleteEntry()
            break
        else:
            clearConsole()
            print("Invalid option. Please choose between the options listed.")

        options()
        choice = input(">> ")
        # BUG Saves choice from first input, and just repeats it every time you press enter. If you press another input, it does not update it.

    else:
        clearConsole()
        print ("You chose to end the program. See you next time.")
        sleep(2)
        quit()

    logout()

class Passwords:
    def __init__(self, username : str, email : str, password : str, notes : str):
        # function for format in passwords.txt
        self.username = username
        self.email = email
        self.password = password
        self.notes = notes

    def pwd_format(self):
        print("-------------------------------")
        print(f"Username: {self.username}")
        print("---")
        print(f"E-mail:     {self.email}")
        print(f"Password:   {self.password}")
        print("---")
        print("Security note:")
        print(self.notes)
        print("-------------------------------")

def pwdList():
    count = 0
    print("\nFull list of all users in the database:\n")
    with open("passwords.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            print(f"User {count}: {line.split('/')[0]}")
        tot = totPwd()
        print()
        print(f"The total number of users currently stored is {tot}.")
    pressEnter()

def login():
    print("Initiating password system...")

    passwords = loadPwd()

    print("Database online.")
    print("All systems online.")

    while True:
        print("Proceed by logging in to your account.\n")
        login.loginUsername = input("\nInput your username: ")
        loginPassword = getpwd("Input your password: ")

        current_user = ""
        for pwd in passwords:
            if loginPassword == pwd.password and login.loginUsername == pwd.username:
                print("\nLogging in...")
                sleep(1)
                current_user = pwd
                break
        else:
            print("\nThe user was not found in our database. The username or password is incorrect. Remember that the input is CAPS-sensitive.")
            logging.warning('Detected login attempt by [{}]: Failed'.format(login.loginUsername))
            continue

        if current_user != "":
            # då har vi kommit åt rätt inloggning
            # Passwords.pwd_format(pwd)
            clearConsole()
            print(f"\nWelcome back, {login.loginUsername}.")
            logging.info('Detected login attempt by [{}]: Succeeded'.format(login.loginUsername))
            menu()

def logout():
    print("\nLogging you out...")
    sleep(1)
    clearConsole()
    print("You have been logged out. Have a wonderful day!")
    
    logging.info('User [{}] have been logged out'.format(login.loginUsername))
    sleep(2)
    clearConsole()

def confirmPass():
    pass
# NOTE is this even necessary?

def createEntry():
    passwords = loadPwd()

    print("\nFill in the form. Note that entering an E-mail is optional.\n")
    
    while True:
        createUsername = input("1. Input a username: ")  
        for pwd in passwords:
            if createUsername == pwd.username:
                print("\nA user with the same name already exists. Please pick another username.\n")
                break
        else:
            break
    
    createEmail = input("3. Input the E-mail of your entry: ")
    if "@" not in createEmail:
        createEmail = "-"
    
    while True:
        createPassword = getpwd("4. Input the password of your entry: ")   
        checkPassword =getpwd("   Please input the same password again: ")
        if checkPassword != createPassword:
            print("Password does not match! Please input the password a second time again.")
            continue
        else:
            break
    
    addNotes = input("5. Would you like to add any notes to your entry? [yes, no]:")

    if "yes".casefold() in addNotes.casefold():
        createNotes = input("Input your notes: ")
    else:
        createNotes = "-"
    
    with open("passwords.txt", "a", encoding="utf8") as x:
        x.write("\n"+createUsername+"/"+createEmail+"/"+createPassword+"/"+createNotes+"/")
    
    print(f"A user by the name of '{createUsername}' was successfully created.")
    logging.info('User [{}] created a new entry in database: {}'.format(login.loginUsername, createUsername))
    viewNow = input("Would you like to view the entry now? [yes, no]: ")
    
    print()
    if "yes".casefold() in viewNow.casefold():
        passwords = loadPwd()
        current_user = ""
        for pwd in passwords:
            if createUsername == pwd.username:
                current_user = pwd
                break
        else:
            print("Error: Could not load entry. Please report this issue to the developer.")
            logging.error('User [{}] tried to view new entry: Failed'.format(login.loginUsername))
            pressEnter()

        if current_user != "":
            # då har vi kommit åt rätt inloggning
            Passwords.pwd_format(pwd)
            pressEnter()
    else:
        pressEnter()

def deleteEntry():
    print("\nNOTE: This will delete the user that you're currently logged in as.\n")
    deleteUserUsername = login.loginUsername
    deleteUserPassword = input("Type your password to confirm your user delete request: ")
    
    passwords = loadPwd()
    current_user = ""   
    for pwd in passwords:
        if deleteUserUsername == pwd.username and deleteUserPassword == pwd.password:
            with open("passwords.txt", "r", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if deleteUserUsername in line:
                        deleteLineUser = [num-1]
            current_user = pwd
            break
    else:
        print("\nPassword does not match. Deletion request could not be fullfilled. Please restart the process from the main menu.")
        logging.warning('User delete request by {}: Denied - Wrong password'.format(login.loginUsername))
        pressEnter()

    if current_user != "":
        # då har vi kommit åt rätt inloggning
        
        lines = []
        
        with open("passwords.txt", "r", encoding="utf8") as f:
            lines = f.readlines()

        with open("passwords.txt", 'w', encoding="utf-8") as f:
            # iterate each line
            for number, line in enumerate(lines):
                if number not in deleteLineUser:
                    f.write(line)

        print(f"User '{deleteUserUsername}' was successfully deleted.")
        logging.info('User delete request by {}: Confirmed'.format(login.loginUsername))
        print("Redirecting you...")
        sleep(5)
    
def findPwd():
    passwords = loadPwd()

    searchUsers = input("\nInput the username you want to search for: ")
    print()
    # TODO Press [X] to go back to the main menu

    current_user = ""    
    for pwd in passwords:
        if searchUsers == pwd.username:
            print("\nFound entry! Loading...\n")
            sleep(1)
            current_user = pwd
            break
    else:
        print("Not found in database. The entry does not exist. Make sure you use CAPS properly.")

    if current_user != "":
        # då har vi kommit åt rätt inloggning
        Passwords.pwd_format(pwd)    
    
    pressEnter()
        
def logRecord():
    test = 1

    # loginAttemptConfirmed = "" DONE
    # loginAttemptDenied = "" DONE
    # passwordChangeConfirmed = ""
    # passwordChangeDenied = ""
    # usernameChangeConformed = ""
    # usernameChangeDenied = ""
    # logoutRequest = "" # TODO person som loggats ut samt när (tid) den gjort det
    # userCreated = ""
    # userDeleted = ""

    #some messages to test
    logger.debug("This is just a harmless debug message") 
    logger.info(f"This is just an information for {test}") 
    logger.warning(f"Detected login attempt by {test}: Login attempt failed.") 
    logger.error("Have you try to divide a number by zero") 
    logger.critical("The Internet is not working....")

def loadPwd():
    logging.info('Database opened')
    password = []
    with open("passwords.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            section = line.split("/")
            pwd = Passwords(section[0],
                            section[1],
                            section[2],
                            section[3])
            
            password.append(pwd)
    return password

def totPwd():
    with open("passwords.txt", "r", encoding="utf8") as f:
        ptot = len(f.readlines())
    return ptot    

def clearConsole():
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def pressEnter():
    print()
    i = input("\nPress Enter to continue\n>> ")
    if "" in i:
        clearConsole()

def main():
    clearConsole()
    login()

if __name__ == "__main__":
    main()