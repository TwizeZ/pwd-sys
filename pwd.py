#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

from time import sleep
from getpwd import getpwd
from operator import itemgetter
import os
import logging
import re

# Format for the logs stored in 'activity.log'.
logging.basicConfig(filename="activity.log", 
                    format='%(asctime)s %(levelname)s %(message)s', 
                    filemode='a', encoding="utf-8", datefmt='%d-%m-%y %H:%M:%S')
logger = logging.getLogger()
# Sets the threshold of logger to INFO
logger.setLevel(logging.INFO)

def options():
    # Options displayed when 'menu' function is called upon.
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
    """Menu

    Choices:
        0: Exits the system completely.
        1: Creates new entry.
        2: Shows list of all entries in database (only their username).
        3: Can help you search for an entry and display its properties (username, e-mail, password (censored), notes).
        4: Logs you out from system.
        usernm: Change your username. Logs you out afterwards.
        passwd: Change your password. Logs you out afterwards.
        delusr: Delete the user currently logged in. Logs you out afterwards. 
    """

    options()
    choice = input(">> ")

    while choice != "0":
        if choice == "1":
            create_entry()
        elif choice == "2":
            pwd_list()
        elif choice == "3":
            find_entry()
        elif choice == "4":
            break
        elif choice == "usernm":
            change_username()
            if change_username == False:
                pass
            else:
                break
        elif choice == "passwd":
            change_password()
            if change_password == False:
                pass
            else:
                break
        elif choice == "delusr":
            delete_entry()
            if delete_entry == False:
                pass
            else:
                break
        else:
            clear_console()
            print("Invalid option. Please choose between the options listed.")

        options()
        choice = input(">> ")

    else:
        clear_console()
        print("You chose to end the program. See you next time.")
        # Logs the successful application exit attempt by user as 'INFO'.
        logging.info(f"User '{login.username}' successfully exited the system.")
        sleep(2)
        quit()

    logout()

class Password:
    def __init__(self, username : str, email : str, password : str, notes : str):
        # function for format in passwords.txt
        """Password properties

        Args:
            username (str): An entry's username. Used to log into the system.
            email (str): The entry's e-mail. Only used for other users to get in contact with a user. Does not serve a purpose in the system itself.
            password (str): The entry's password. Used to log into the system.
            notes (str): Additional notes tied to an entry. Does not serve a purpose in the system itself.
        """

        self.username = username
        self.email = email
        self.password = password
        self.notes = notes

    def pwd_format(self):
        pwd_hidden = '*' * len(self.password)
        print("-------------------------------")
        print(f"Username: {self.username}")
        print("---")
        print(f"E-mail:     {self.email}")
        print(f"Password:   {pwd_hidden}")
        print("---")
        print("Security note:")
        print(self.notes)
        print("-------------------------------")
        # Logs the user viewing another user's entry as 'INFO'.
        logging.info(f"User '{login.username}' is viewing the entry of user '{self.username}'")

def pwd_list():
    # Logs the user viewing the full entrylist as 'INFO'.
    logging.info(f"User '{login.username}' is viewing an entire list of all users in the database")
    count = 0
    print("\nFull list of all users in the database:\n")
    with open("passwords.txt", "r", encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            print(f"User {count}: {line.split('/')[0]}")
        tot = tot_entries()
        print()
        print(f"The total number of users currently stored is {tot}.")
    proceed()

def login():
    print("Initiating password system...")
    while True:
        database = load_db()
        print("All systems online.")

        print("Proceed by logging in to your account.\n")
        login.username = input("\nInput your username: ")
        login.password = getpwd("Input your password: ")

        current_user = ""
        for pwd in database:
            if login.password == pwd.password and login.username == pwd.username:
                print("\nLogging in...")
                sleep(1)
                current_user = pwd
                break
        else:
            print("\nThe user was not found in our database. The username or password is incorrect. Remember that the input is CAPS-sensitive.\n")
            # Logs the unsuccessful login attempt as 'WARNING'.
            logging.warning(f"Detected login attempt by user '{login.username}': Failed")
            continue

        if current_user != "":
            # Passwords.pwd_format(pwd)
            clear_console()
            print(f"\nWelcome back, {login.username}.")
            # Logs the successful login attempt as 'INFO'.
            logging.info(f"Detected login attempt by user '{login.username}': Succeeded")
            menu()

def logout():
    print("\nLogging you out...")
    sleep(1)
    clear_console()
    print("You have been logged out. Have a wonderful day!")
    # Logs the successful logout attempt by user as 'INFO'.
    logging.info(f"User '{login.username}' have been logged out")
    sleep(2)
    clear_console()

def create_entry():
    database = load_db()

    print("\nFill in the form. Note that entering an E-mail is optional. You cannot use '/' in any of your inputs.\n")
    
    while True:
        invalid_name = 0
        create_username = input("1. Input a username: ")  
        for pwd in database:
            if create_username == pwd.username:
                print("\nA user with the same name already exists. Please pick another username.\n")
                invalid_name = 1
                break
        if invalid_name == 1:
            continue
        elif "/" in create_username:
            print("\nYour username cannot include the symbol '/'.\n")
            continue
        elif create_username == "":
            print("\nYou need a username. Do not leave this empty.\n")
            continue
        else:
            break
    
    while True:
        create_email = input("\n2. Input the E-mail of your entry (optional): ")
        if "/" in create_email:
            print("\nYour e-mail cannot include the symbol '/'.\n")
            continue
        elif "@" not in create_email or create_email == "":
            create_email = "-"
            break
        else:
            break
    
    while True:
        create_password = getpwd("\n3. Input the password of your entry: ")   
        check_password =getpwd("Please input the same password again: ")
        if check_password != create_password:
            print("\nPassword does not match! Please input the password a second time again.\n")
            continue
        elif "/" in create_password:
            print("\nYour password cannot include the symbol '/'.\n")
            continue
        elif create_password == "":
            print("\nYou need a password. Do not leave this empty.\n")
            continue
        else:
            break
    
    add_notes = input("\n4. Would you like to add any notes to your entry? [yes, no]: ")

    if "yes".casefold() in add_notes.casefold():
        while True:
            create_notes = input("\nInput your notes: ")
            if "/" in create_notes:
                print("\nYour notes cannot include the symbol '/'.\n")
                continue
            elif create_notes == "":
                create_notes = "-"
                break
            else:
                break
    else:
        createNotes = "-"
    
    with open("passwords.txt", "a", encoding="utf8") as x:
        x.write(create_username+"/"+create_email+"/"+create_password+"/"+create_notes+"/"+"\n")
    
    print(f"\nA user by the name of '{create_username}' was successfully created.\n")
    # Logs the successful entry creation as 'INFO'.
    logging.info(f"User '{login.username}' created a new entry in database: '{create_username}'")
    view_entry = input("Would you like to view the entry now? [yes, no]: ")
    
    print()
    if "yes".casefold() in view_entry.casefold():
        database = load_db()
        current_user = ""
        for pwd in database:
            if create_username == pwd.username:
                current_user = pwd
                break

        if current_user != "":
            Password.pwd_format(pwd)
            proceed()
    else:
        proceed()

def delete_entry():
    print("\nNOTE: This will delete the user that you're currently logged in as.\n")
    username = login.username
    password = getpwd("Type your password to confirm your user delete request: ")
    
    database = load_db()
    current_user = ""   
    for pwd in database:
        if username == pwd.username and password == pwd.password:
            with open("passwords.txt", "r", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if username in line:
                        delete_line = [num-1]
            current_user = pwd
            break
    else:
        print("\nPassword does not match. Deletion request could not be fullfilled. Please restart the process from the main menu.")
        # Logs the unsuccessful user deletion as 'WARNING'.
        logging.warning(f"User delete request by {username}: Denied - Wrong password")
        proceed()
        return False

    if current_user != "":
        # The original entry currently logged in was found in the database.

        # Empty list to temporarily store the database in.
        lines = []
        # Receives and places the database in the temporarily list.
        with open("passwords.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
        # Deletes all entries in database, and puts back all entries that were not supposed to be deleted.
        with open("passwords.txt", 'w', encoding="utf-8") as f:
            for number, line in enumerate(lines):
                if number not in delete_line:
                    f.write(line)

        print(f"\nUser '{username}' was successfully deleted.\n")
        # Logs the successful user deletion as 'INFO'.
        logging.info(f"User delete request by {username}: Confirmed")
        print("Redirecting you...")
        sleep(3)
        return True
    
def change_password():
    
    username = login.username

    current_password = getpwd("\nInput your current password: ")
    print()

    database = load_db()

    # Identifies the entry in the database.
    current_user = ""   
    for pwd in database:
        if username == pwd.username and current_password == pwd.password:
            with open("passwords.txt", "r", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if current_password in line:
                        entryline_list = [num-1]
                        entryline_int = int(num-1)
            current_user = pwd
            break
    else:
        print("\nPassword does not match. Password could not be changed. Please restart the process from the main menu.\n")
        # Logs the unsuccessful password change as 'WARNING'.
        logging.warning(f"Password change request by {username}: Denied - Wrong password")
        proceed()
        return False
    

    if current_user != "":
        # The original entry currently logged in was found in the database.

        # Retrieves username, e-mail, and notes from entry in database
        with open("passwords.txt", "r", encoding="utf-8") as file:
            counter = 0
            while (entries := file.readline().rstrip()):
                counter += 1
                if counter > entryline_int:
                    break
        
        # Takes the correct entry and makes it into a list 
        entry = [entries]
        # Splits the 'entry' list in to multiple items in the list in order to pick out certain items from that list.
        split_list = [item for string in entry for item in re.split("(/)", string)]
        # Removes the separations in the entry ('/').
        while "/" in split_list:
            split_list.remove('/')
        split_list.remove('')

        # Gets the current username from the list
        original_username = itemgetter(0)(split_list)
        # Gets the current e-mail from the list
        original_email = itemgetter(1)(split_list)
        # Gets the current notes from the list
        original_notes = itemgetter(3)(split_list)
        
        # Your new password input
        while True:
            new_password = getpwd("\nInput your new password: ")
            check_password =getpwd("\nInput your new password again: ")
            if check_password != new_password:
                print("\nPassword does not match! Please input the password a second time again.\n")
                continue
            elif "/" in new_password:
                print("\nYour password cannot include the symbol '/'.\n")
                continue
            elif new_password == "":
                print("\nYou need a password. Do not leave this empty.\n")
                continue
            else:
                break
        
        print()
        
        # Empty list to temporarily store the database in.
        lines = []
        # Receives and places the database in the temporarily list.
        with open("passwords.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
        # Deletes all entries in database, and puts back all entries that were not supposed to be modified.
        with open("passwords.txt", 'w', encoding="utf-8") as f:
            for number, line in enumerate(lines):
                if number not in entryline_list:
                    f.write(line)
            # Creates a new entry based on all information in the old one, except with your new password.
            f.write(original_username+"/"+original_email+"/"+new_password+"/"+original_notes+"/"+"\n")
                    

        print(f"\nPassword for user '{username}' was successfully changed.")
        # Logs the successful password change as 'INFO'.
        logging.info(f"Password change request by {username}: Confirmed - New password: {new_password}")
        proceed()
        return True

def change_username():
    
    current_username = login.username

    password = getpwd("\nInput your password: ")
    print()

    database = load_db()

    # Identifies the entry in the database.
    current_user = ""   
    for pwd in database:
        if current_username == pwd.username and password == pwd.password:
            with open("passwords.txt", "r", encoding="utf-8") as myFile:
                for num, line in enumerate(myFile, 1):
                    if password in line:
                        entryline_list = [num-1]
                        entryline_int = int(num-1)
            current_user = pwd
            break
    else:
        print("\nPassword does not match. Password could not be changed. Please restart the process from the main menu.\n")
        # Logs the unsuccessful name change as 'WARNING'.
        logging.warning(f"Username change request by {current_username} denied: Wrong password")
        proceed()
        return False
    

    if current_user != "":
        # The original entry currently logged in was found in the database.

        # Retrieves password, e-mail, and notes from entry in database.
        with open("passwords.txt", "r", encoding="utf-8") as file:
            counter = 0
            while (entries := file.readline().rstrip()):
                counter += 1
                if counter > entryline_int:
                    break
        
        # Takes the current entry and makes it into a list 
        entry = [entries]
        # Splits the 'entry' list in to multiple items in the list in order to pick out certain items from that list.
        split_list = [item for string in entry for item in re.split("(/)", string)]
        # Removes the separations in the entry ('/').
        while "/" in split_list:
            split_list.remove('/')
        split_list.remove('')

        # Gets the current password from the list
        original_password = itemgetter(2)(split_list)
        # Gets the current e-mail from the list
        original_email = itemgetter(1)(split_list)
        # Gets the current notes from the list
        original_notes = itemgetter(3)(split_list)
        
        # Your new username input
        while True:
            invalid_name = 0
            new_username = input("\nInput your new username: ")
            
            # Checks that the username is not already taken. If not, it proceeds.
            for pwd in database:
                if new_username == pwd.username:
                    print("\nThat username is already in use. Please choose a different username.\n")
                    invalid_name = 1
                    break
            if invalid_name == 1:
                continue
            elif "/" in new_username:
                print("\nYour username cannot include the symbol '/'.\n")
                continue
            elif new_username == "":
                print("\nYou need a username. Do not leave this empty.\n")
                continue
            else:
                break
        
        print()
        
        # Empty list to temporarily store the database in.
        lines = []
        # Receives and places the database in the temporarily list.
        with open("passwords.txt", "r", encoding="utf8") as f:
            lines = f.readlines()
        # Deletes all entries in database, and puts back all entries that were not supposed to be modified.
        with open("passwords.txt", 'w', encoding="utf-8") as f:
            for number, line in enumerate(lines):
                if number not in entryline_list:
                    f.write(line)
            # Creates a new entry based on all information in the old one, except with your new username.
            f.write(new_username+"/"+original_email+"/"+original_password+"/"+original_notes+"/"+"\n")
                    

        print(f"\nUsername for '{current_username}' was successfully changed to {new_username}.")
        # Logs the successful name change as 'INFO'.
        logging.info(f"User '{current_username}' successfully changed their username to {new_username}")
        proceed()
        return True

def find_entry():
    database = load_db()

    while True: # TODO Fix this while-loop.
        search_username = input("\nInput the username you want to search for: ")
        print()

        current_user = ""    
        for pwd in database:
            if search_username == pwd.username:
                print("\nFound entry! Loading...\n")
                sleep(1)
                current_user = pwd
                break
        else:
            print("\nNot found in database. The entry does not exist. Make sure you use CAPS properly.\n")
            

    if current_user != "":
        # då har vi kommit åt rätt inloggning
        Password.pwd_format(pwd)    
    
    proceed()

def load_db():
    """Loads database

    Returns:
        entry: Includes username, e-mail, password, and notes.
    """

    # Logs when database is loaded as 'INFO'.
    logging.info("Entire database loaded")
    password = []
    with open("passwords.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            section = line.split("/")
            pwd = Password(section[0],
                            section[1],
                            section[2],
                            section[3])
            
            password.append(pwd)
    return password

def tot_entries():
    with open("passwords.txt", "r", encoding="utf8") as f:
        ptot = len(f.readlines())
    return ptot    

def clear_console():
    # Function to clear the console. Both used for aestethical and security-related reasons.
    command = "clear"
    if os.name in ("nt", "dos"):
        command = "cls"
    os.system(command)

def proceed():
    # Function used when the user is done using a feature.
    print()
    i = input("\nPress Enter to continue.\n>> ")
    if "" in i:
        clear_console()

def main():
    clear_console()
    login()

if __name__ == "__main__":
    main()