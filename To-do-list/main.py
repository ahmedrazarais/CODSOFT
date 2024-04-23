# TO-DO LIST
# TASK 1
# A To-Do List application is a useful project that helps users manage
# and organize their tasks efficiently. This project aims to create a
# command-line or GUI-based application using Python, allowing
# users to create, update, and track their to-do list

from register_class import Registration
from login_class import Login
from user_class import Users

registration=Registration()
login=Login()
users=Users()



def main():
    print('\n\t"Welcome To Task-Tracker"')
    print("\tOnce You Login you would able to enter in Task-Tracker")
    print("------------------------------------------------")
    while True:
            # Display options
            print("\t1.Register Yourself.")
            print("\t2.Login Into Account.")
            print("\t3.Exit: To exit from Task-Tracker.\n\n")

            # Get user choice
            get_choice = input("Enter Your Choice in Task-Tracker:").strip()

            # Manage choices
            if get_choice == "1":
                print("\tWelcome To Registration Area")
                registration.registration_process()

            elif get_choice == "2":
                print("\tWelcome To Login Area")
                users.main_page()

            elif get_choice == "3":
                print("Task-Tracker is exiting now. See you soon...\n")
                print("Good Bye!!")
                exit()  # Terminate the program

            else:
                print("\nInvalid Choice. Please select from the given choices.\n")


main()
