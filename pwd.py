#Felix Larsson
#TEINF-20
#Password System
#11-05-2022

import random
# from time import sleep
   

class Passwords:
    def __init__(self, name : str, username : str, email : str, password : str, notes : str):
        # def for format in passwords.txt
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.notes = notes
        # self.created = created



def load_question():
    questions = []
    with open("passwords.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            selection = line.split("/")
            pwd = Passwords(selection[0],
                            selection[1],
                            selection[2].split(","))
            
            questions.append(pwd)
    return questions

def question_quantity():
    with open("passwords.txt", "r", encoding="utf8") as fp:
        qtot = len(fp.readlines())
    return qtot    



def main():
    pass

if __name__ == "__main__":
    main()