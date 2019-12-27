# Author      : Isaiah Jared
# Description : Simple CLI login system

import sys
import os
import hashlib

userOS = str(sys.platform)


# This function exists so that the user doesn't have to deal with visual clutter in the command-line
def clearFunc():
    if "win32" not in userOS:
        os.system('clear')
    else:
        os.system('cls')


# The first menu is set in its own function in order to take the user to the appropriate section (whether it's making a new account or logging into a pre-existing one)
def intro():
    print("Welcome to the ISN Login System!")
    try:
        optSelect = int(
            input("Use 1-3 to select from the options below:\n1. Login\n2. Register an Account\n3. Exit\n\n"))
        if optSelect == 1:
            clearFunc()
            loginFunc()
        elif optSelect == 2:
            clearFunc()
            registerFunc()
        elif optSelect == 3:
            clearFunc()
            sys.exit(0)
        else:
            input("Something broke :^)")
    except ValueError:
        input(
            "Invalid input type! You must enter an integer between 1-3 to make your selection! (press Enter to return): ")
        clearFunc()
        intro()



def loginFunc():
    print("====== ISN Login =======\n")
    userName = input("Username: ")
    passWord = input("Password: ")

    # Allows the program to grab the user's information which is stored as an SHA256 hash; also since the userName + passWord vars are one line, it makes it easier for the program to iterate through and find the appropriate credentials if they do not exist

    str = hashlib.sha256(userName.encode('utf-8'))
    nameHashed = str.hexdigest()

    str = hashlib.sha256(passWord.encode('utf-8'))
    passHashed = str.hexdigest()


    userSearch = nameHashed + " : " + passHashed
    print(userSearch)

    # Could utilize a more elegant solution
    fobj = open("stored.txt")
    text = fobj.readlines()
    if userSearch in text:
        fobj.close()
        print("You have successfully logged in: {}".format(userName))
        input("Press any key to exit: ")
        sys.exit(0)
    else:
        input("Invalid/non-existent credentials. Please press any key to return to the main menu: ")
        fobj.close()
        clearFunc()
        intro()


def registerFunc():
    print("====== ISN Registration Form =======\n")
    print("Please enter the required information below to register your account!\n\n")
    registerName = input("Username (minimum 6 characters): ")

    if len(registerName) < 6:
        clearFunc()
        input("Username too short! It must have a length of 6 or more characters. Press Enter to return: ")

        clearFunc()
        registerFunc()

    else:
        registerPassWord = input("Password (minimum 6 characters): ")

        if len(registerPassWord) < 6:
            clearFunc()
            input("Password too short! It must have a length of 6 or more characters. Press Enter to return: ")

            clearFunc()
            registerFunc()

        else:
            confirmPass = input("Confirm password: ")
            if confirmPass != registerPassWord:
                clearFunc()
                input("Password does not match! Press Enter to return: ")

                clearFunc()
                registerFunc()
            else:
                # Taking the username and password; converting it to sha256, then storing them into a .txt or database! Implement more complex hashing later perhaps?
                str = hashlib.sha256(registerName.encode('utf-8'))
                nameHashed = str.hexdigest()

                str = hashlib.sha256(registerPassWord.encode('utf-8'))
                passHashed = str.hexdigest()

                storedAccount = nameHashed + " : " + passHashed
                if not os.path.exists("stored.txt"):
                    with open("stored.txt", "w") as file:
                        file.write("{}".format(storedAccount))
                else:
                    with open("stored.txt", "a") as file:
                        file.write("\n{}".format(storedAccount))

                clearFunc()
                finalStep = int(input("Account has been successfully registered into the ISN system! Choose what action you would like to take next: \n1. Login\n2. Exit\n"))
                if finalStep == 1:
                    loginFunc()
                else:
                    sys.exit(0)

intro()
