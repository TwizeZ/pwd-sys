#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

from time import sleep
from getpwd import getpwd
import os

class Menu:
    def options():
        print()
        print("[1] Create new entry.")
        print("[2] List of all entries.")
        print("[3] Search entries.")
        print("[4] Settings.")
        print("[5] Log out.")
        print("[0] Exit application.")

    def option_1():
        print()
        print ("Please fill in all following inputs.\n")
        createEntry()

    def option_2():
        # print ("Input the name of the current account. If you would like to see a list of all entries, please input [X].")
        print()
        print ("Here is a list of all your entries stored in your local database.\n")
        pwdList()
    
    def option_3():
        print()
        print("Input the name of the account. Input [X] to view, or [Y] to edit entry. You can delete the account by selecting [Z].\n")
        findPwd()

    def menu():
        Menu.options()
        choice = input(">> ")

        while choice != "0":
            if choice == "1":
                Menu.option_1()
            elif choice == "2":
                Menu.option_2()
            elif choice == "3":
                Menu.option_3()
            elif choice == "4":
                settings()
            elif choice == "5":
                logout()
            elif choice == "0":
                break
            # BUG Does not exit application, only logs you out
            else:
                clearConsole()
                print("Invalid option. Please choose between the options listed.")

            Menu.options()
            choice == input(">> ")
            # BUG Saves choice from first input, and just repeats it every time you press enter. If you press another input, it does not update it.

        else:
            clearConsole()
            print ("You chose to end the program. See you next time.")

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
    # NOTE Denna funktion borde läsa in alla lösenord i "databasen" och lagra i programmet - bör byta om funktionen då den inte gör detta
    # TODO Merge with loadPwd() function? 
    print("Initiating password system...")

    passwords = loadPwd()
    
    print("Database online.")
    print("All systems online.")
    print("Proceed by logging in to your account.")

    while True:
        uUsername = input("\nInput your username: ")
        uPassword = getpwd("Input your password: ")

        current_user = ""
        for pwd in passwords:
            if uPassword == pwd.password and uUsername == pwd.username:
                print("\nLogging in...")
                sleep(1.5)
                current_user = pwd
                break
        else:
            print("\nThe user was not found in database. The username or password is incorrect.")
            continue

        if current_user != "":
            # då har vi kommit åt rätt inloggning
            # Passwords.pwd_format(pwd)
            clearConsole()
            print(f"\nWelcome back, {uUsername}.")
            Menu.menu()

def logout():
    print("\nLogging you out...")
    sleep(1.5)
    clearConsole()
    print("You have been logged out. Have a wonderful day!")
    sleep(3)
    clearConsole()
    login()

def createEntry():
    current_user = ""
    passwords = loadPwd()
    
    while True:
        eusername = input("1. Input your username: ")  
        for pwd in passwords:
            if eusername == pwd.username:
                print("\nA user with the same name already exists. Please pick another username.\n")
                break
        else:
            break
    
    # eusername = input("2. Input the username of your entry (not your E-mail): ")
    eemail = input("3. Input the E-mail of your entry: ")
    epassword = input("4. Input the password of your entry: ")
    
    #NOTE Ask to input password a second time to be sure it is spelled correctly
    
    # while True:
    #     epassword2 =input("   Please input the same password again: ")
    #     if epassword2 != epassword:
    #         print("Password does not match! Please input the password a second time again.")
    #         continue
    #     else:
    #         break
    
    enotes = input("5. Would you like to add any notes to your entry? [yes, no]:")

    if "yes".casefold() in enotes.casefold():
        enotes = ""
        enotes = input("Input your notes: ")
    else:
        enotes = ""
        enotes = "-"
    
    with open("passwords.txt", "a", encoding="utf8") as x:
        x.write("\n"+eusername+"/"+eemail+"/"+epassword+"/"+enotes+"/")
    
    print(f"A user by the name of '{eusername}' was successfully created.")
    viewNow = input("Would you like to view the entry now? [yes, no]:")
    
    print()
    if "yes".casefold() in viewNow.casefold():
        current_user = ""
        for pwd in passwords:
            if eusername == pwd.username:
                current_user = pwd
                break
        else:
            print("Error: Could not load entry. Please report this issue to the developer.")

        if current_user != "":
            # då har vi kommit åt rätt inloggning
            Passwords.pwd_format(pwd)
            pressEnter()
    else:
        pressEnter()

def deleteEntry():
    deleteEntry = input("Type the name of the entry to confirm that you want to delete the entry: ")
    # TODO Add if-sats to check that deleteEntry is the same as the one currently displayed.

    with open("passwords.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
    with open("passwords.txt", "w", encoding="utf8") as f:
        for line in lines:
            if line.strip("\n") != deleteEntry:
                f.write(line)

def editEntry():
    choice = input("What you you like to edit in your entry?\n>> ")
    
    print("[1] Username.")
    print("[2] E-mail.")
    print("[3] Password.")
    print("[4] Notes.")
    print()
    print("[0] Back to main menu.")
    
    if choice == "1":
        changeUsername = input("What would you like to change the username to?: ")
    elif choice == "2":
        changeEmail = input("What would you like to change the E-mail to?: ")
    elif choice == "3":
        changePassword = input("What would you like to change the password to?: ")
    elif choice == "4":
        changeNotes = input("What notes would you like to add?: ")
    else:
        clearConsole()
        Menu.menu()

def settings():
    print("This is the settings page. Please input one of the following commands to edit certain settings.")
    print("Change password - 'passwd'")
    print("Change username - 'usern'")
    
def findPwd():
    passwords = loadPwd()

    searchUsers = input("Input the username you want to search for: ")
    # TODO Press [X] to go back to the main menu

    current_user = ""    
    for pwd in passwords:
        if searchUsers == pwd.entry:
            print("\nFound entry! Loading...\n")
            sleep(1.5)
            current_user = pwd
            break
    else:
        print("Not found in database. The entry does not exist. Make sure you use CAPS properly.")

    if current_user != "":
        # då har vi kommit åt rätt inloggning
        Passwords.pwd_format(pwd)    
    
    pressEnter()

def loadPwd():
    passwords = []
    with open("passwords.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            section = line.split("/")
            pwd = Passwords(section[0],
                            section[1],
                            section[2],
                            section[3])
            
            passwords.append(pwd)
    return passwords

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
    print("\nPress Enter to go back to the main menu")
    i = input(">> ")
    if "" in i:
        clearConsole()

def main():
    login()

if __name__ == "__main__":
    main()