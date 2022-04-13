#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

from time import sleep
   

class Passwords:
    def __init__(self, name : str, username : str, email : str, password : str, notes : str):
        # def for format in passwords.txt
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.notes = notes
        # self.created = created

    def pwd_info(self):
        print(f"Name:       {self.name}")
        print("---")
        print(f"Username:   {self.username}")
        print(f"E-mail:     {self.email}")
        print(f"Password:   {self.password}")
        print("---")
        print("Additional notes:")
        print(self.notes)

class Begin:
    def start_sys(self):        
        print("Initiating password system...")
        sleep(2)
        print("Database online.")
        
    
        search = input("Input name of password: ")
        
        file = open('passwords.txt', 'r', encoding='utf8')
        
        flag = 0
        index = 0

        for line in file:
            index += 1

            if search in line:
                flag = 1
                break
        
        if flag == 0:
            print(f"{search} was not found.")
        else:
            print(f"{search} was found in line {index}")
            self.name = load_pwd()
            
            for info in range(index):
                self.name[info].pwd_info()


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
    Begin().start_sys()

if __name__ == "__main__":
    main()