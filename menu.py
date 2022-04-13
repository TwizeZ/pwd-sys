#Felix Larsson
#TEINF-20
#Password System
#11-05-2022


def options():
    print("[1] Create new entry.")
    print("[2] Edit entry.")
    print("[3] Search entries.")
    print("[0] Exit application.")

def option_1():
    print ("Name your new entry. This should be the name of the website where you created your new account.")

def option_2():
    print ("Input the name of the current account. If you would like to see a list of all entries, please input [X].")

def option_3():
    print ("Input the name of the account. Input [X] to view, or [Y] to edit entry. You can delete the account by selecting [Z].")

def menu():
    options()
    choice = input(">> ")

    while choice != "0":
        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please choose between the options listed.")
        
        options()
        choice = input(">> ")

    else:
        print ("You chose to end the program.")

def main():
    menu()

if __name__ == "__main__":
    main()