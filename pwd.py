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
        print("[0] Exit application.")

    def option_1():
        print()
        print ("Please fill in all following inputs.\n")
        Managing.create_entry()

    def option_2():
        # print ("Input the name of the current account. If you would like to see a list of all entries, please input [X].")
        print()
        print ("Here is a list of all your entries stored in your local database.\n")
        Passwords.pwd_list()
    
    def option_3():
        print()
        print("Input the name of the account. Input [X] to view, or [Y] to edit entry. You can delete the account by selecting [Z].\n")
        find_pwd()

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
            elif choice == "0":
                break
            else:
                print("Invalid option. Please choose between the options listed.")
            
            Menu.options()
            choice = input(">> ")

        else:
            clearConsole()
            print ("You chose to end the program. See you next time.")

class Passwords:
    def __init__(self, entry : str, username : str, email : str, password : str, notes : str):
        # function for format in passwords.txt
        self.entry = entry.casefold()
        self.username = username
        self.email = email
        self.password = password
        self.notes = notes
        # self.created = created

    def pwd_format(self):
        print("-------------------------------")
        print(f"Entry Name: {self.entry}")
        print("---")
        print(f"Username:   {self.username}")
        print(f"E-mail:     {self.email}")
        print(f"Password:   {self.password}")
        print("---")
        print("Additional notes:")
        print(self.notes)
        print("-------------------------------")

    def pwd_list():
        count = 0
        with open("passwords.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                count += 1
                print("Entry {}: {}".format(count, line.strip()))
        pressEnter()

class Managing:
    def create_entry():
        current_user = ""
        
        eentry = input("1. Input the entry name: ")
        eusername = input("2. Input the username of your entry (not your E-mail): ")
        eemail = input("3. Input the E-mail of your entry: ")
        epassword = input("4. Input the password of your entry: ")
        enotes = input("5. Would you like to add any notes to your entry? [yes, no]:")

        if "yes".casefold() in enotes.casefold():
            enotes = ""
            enotes = input("Input your notes: ")
        else:
            enotes = ""
            enotes = "-"
        
        with open("passwords.txt", "a", encoding="utf8") as x:
            x.write("\n"+eentry+"/"+eusername+"/"+eemail+"/"+epassword+"/"+enotes+"/") #f"{name}\n"

        passwords = load_pwd()
        viewNow = input(f"'{eentry}' entry successfully created. Would you like to view the entry now? [yes, no]:")
        print()
        if "yes" in viewNow:
            current_user = ""
            for pwd in passwords:
                if eentry.casefold() == pwd.entry:
                    current_user = pwd
                    break
            else:
                print("Error: Could not load entry.")

            if current_user != "":
                # då har vi kommit åt rätt inloggning
                Passwords.pwd_format(pwd)
                pressEnter()
        else:
            pressEnter()

    def delete_entry():
        pass

    def edit_entry():
        pass



def start_sys():
    # NOTE Denna funktion borde läsa in alla lösenord i "databasen" och lagra i programmet - bör byta om funktionen då den inte gör detta
    # Merge with load_pwd() function?
    print("Initiating password system...")
    sleep(1.5)
    print("Database online.")
    
def find_pwd():
    passwords = load_pwd()

    # search_name = input("Input your username: ")
    # search_pwd = getpwd("Input your password: ")
    search_entry = input("Input your entry name: ")
    
    current_user = ""
    # for pwd in passwords:
    #     if search_pwd == pwd.password and search_name == pwd.username:
    #         print("Found entry!")
    #         current_user = pwd
    #         break
    # else:
    #     print("Not found in database. The username or password is incorrect.")
    
    for pwd in passwords:
        if search_entry.casefold() == pwd.entry:
            print("\nFound entry! Loading...\n")
            sleep(1.5)
            current_user = pwd
            break
    else:
        print("Not found in database. The entry does not exist.")

    if current_user != "":
        # då har vi kommit åt rätt inloggning
        Passwords.pwd_format(pwd)

        
            # for info in range(index):
                # self.name[info].pwd_format()


            # if search in passwords:
            #     Passwords().pwd_format()
            # else:
            #     print("No such password was found.")
            #     continue
    
    
    # NOTE Sätt in "What would you like to do?" meny, med alternativ så som edit, delete och back to main menu
    # Separationsfunktion för att rensa hela terminalen
    pressEnter()

def load_pwd():
    passwords = []
    with open("passwords.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            section = line.split("/")
            pwd = Passwords(section[0],
                            section[1],
                            section[2],
                            section[3],
                            section[4])
            
            passwords.append(pwd)
    return passwords

# pwd_quantity not currently utilized
def pwd_quantity():
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
    start_sys()
    Menu.menu()

if __name__ == "__main__":
    main()