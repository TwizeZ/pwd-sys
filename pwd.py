#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

from time import sleep
from getpwd import getpwd

class Passwords:
    def __init__(self, entry : str, username : str, email : str, password : str, notes : str):
        # function for format in passwords.txt
        self.entry = entry
        self.username = username
        self.email = email
        self.password = password
        self.notes = notes
        # self.created = created

    def pwd_info(self):
        print(f"Entry Name: {self.entry}")
        print("---")
        print(f"Username:   {self.username}")
        print(f"E-mail:     {self.email}")
        print(f"Password:   {self.password}")
        print("---")
        print("Additional notes:")
        print(self.notes)

def start_sys():
    # Denna funktion borde läsa in alla lösenord i "databasen" och lagra i programmet - bör byta om funktionen då den inte gör detta
    print("Initiating password system...")
    sleep(1)
    print("Database online.")
    find_pwd()
    
def find_pwd():
    passwords = load_pwd()

    search_name = input("Input your username: ")
    search_pwd = getpwd("Input your password: ")
    current_user = ""
    for pwd in passwords:
        if search_pwd == pwd.password and search_name == pwd.username:
            print("Found entry!")
            current_user = pwd
            break
    else:
        print("Not found in database. The username or password is incorrect.")
    
    if current_user != "":
        # då har vi kommit åt rätt inloggning
        Passwords.pwd_info(pwd)

        # edit entry information - will be moved to new function
        edit_entry = input("Would you like to edit any information found in this entry? [yes, no]: ")

        if "yes" in edit_entry:
            pass
        else:
            pass        
        
            # for info in range(index):
                # self.name[info].pwd_info()


            # if search in passwords:
            #     Passwords().pwd_info()
            # else:
            #     print("No such password was found.")
            #     continue
        

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

def pwd_quantity():
    with open("passwords.txt", "r", encoding="utf8") as f:
        ptot = len(f.readlines())
    return ptot    



def main():
    start_sys()

if __name__ == "__main__":
    main()