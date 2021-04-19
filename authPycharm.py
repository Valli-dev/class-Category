import random
import datetime
import database
import validation
import withdraw
from getpass import getpass

balance = 0
flag = 0
def init():
    print("******************* WELCOME TO BANK PHP **********************")

    try:
        haveaccount = int(input("Do you have account with us? 1 (Yes) 2 (No) 3(exit)\n"))
        if (haveaccount == 1):
            login()
        elif (haveaccount == 2):
            register()
        elif (haveaccount == 3):
            exit()

        else:
            print("enter valid option\n")
            init()

    except ValueError:
        print("Value Error: please enter a valid option\n")
        init()



def register():
    print("********* New Account opening Registration: ********** \n")

    firstName = input("Enter your first name: \n")
    lastName = input("Enter your Last name: \n")
    email = input("Enter your email address: \n")
    password = getpass("Please create your password:\n")

    balance = input("please enter the amount you deposit:\n")

    accountNumber = generateAccountNumber()


    isAccountCreated = database.create(accountNumber, firstName, lastName, balance, password, email)


    if isAccountCreated:

        print("\nYour Account has been created successfully")
        print("**************Login details********************\n")
        print("Your account number is ", accountNumber)
        print("Make sure to keep it safe")
        print("************************************************\n")
        #login()
        init()
    else:
        print("Something went wrong\n Please try again")
        #register()



def login():


    x = datetime.datetime.now()

    accountNumberFromUser = input("\nWhat is your Account Number?\n")

    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)


    if not isValidAccountNumber:
        print("Invalid Account number")
        init()
    else:
        password = getpass("\nWhat is your password?\n")


        is_db_authenticated_user = database.authentication(accountNumberFromUser, password)
        print(is_db_authenticated_user)


        if is_db_authenticated_user:

             session_login = database.auth_sessionlogin(accountNumberFromUser)

             if session_login:
                print("**************Login successful*************** @ ", x)

                bankOperation(accountNumberFromUser, is_db_authenticated_user)
                init()

        else:
            print("authentication failed:")
            init()



def bankOperation(acNumber, user):
    print("Welcome %s %s !!!!\n" % (user[0], user[1]))

    try:

        selectedOption = int(input(" What would you like to do?\n Bank operations:\n 1. Withdrawal\n 2. Cash Deposit\n 3. Check balance\n 4. logout Account \n 5. Exit Bank operations\n "))


        if (selectedOption == 1):

            amount= input("Enter the amount to withdraw:\n")

            newbalance = database.withdraw(acNumber, amount)


            '''session_logout = database.auth_session_logout(acNumber)
            if session_logout:
                print("Logging OUT of your account!\n") '''



        elif (selectedOption == 2):

            amount = input("Enter the amount to deposit:\n")
            x=database.deposit(acNumber, amount)

            '''session_logout = database.auth_session_logout(acNumber)
            if session_logout:
                print("Logging OUT of your account!\n")'''



        elif (selectedOption == 3):

            balance = database.getbalance(acNumber)
            user_list = str.split(balance, ',')
            print("Current Balance in your account is", user_list[2])


        elif (selectedOption == 4):


            session_logout = database.auth_session_logout(acNumber)
            if session_logout:
                print("Logging OUT of your account!\n")

            init()

        elif (selectedOption == 5):
            print("Quit Bank Operations\n")
            session_logout = database.auth_session_logout(acNumber)
            if session_logout:
                print("Logging OUT of your account!\n")
                exit()
        else:
            print("Invalid option\n")


            #bankOperation(user)

    except ValueError:
        print("ValueError: Enter valid option\n")
        bankOperation(acNumber,user)


    return

def generateAccountNumber():
    print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)


####ACTUAL BANKING SYSTEM######

init()



