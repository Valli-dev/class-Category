import random
import datetime



userDatabase = {1111111111: ['Seyi', 'Onifade', 'seyionifade@zuriteam.com', 'PasswordSeyi', 1000],
                2222222222: ["Mike", "Koss", "mikekoss@zuriteam.com", "PasswordMike", 1500],
                3333333333: ["Valli", "Mayil", "vallimayil@gmail.com", "PasswordMayil", 1200]}

balance = 0
def init():
    print("******************* WELCOME TO BANK PHP **********************")
    haveaccount = int(input("Do you have account with us? 1 (Yes) 2 (No) 3(exit)\n"))
    if (haveaccount == 1):
        login()
    elif (haveaccount == 2):
        register()
    elif (haveaccount == 3):
        exit()
    else:
        print("please enter a valid option")
        init()


def register():
    print("********* New Account opening Registration: ********** \n")

    firstName = input("Enter your first name: \n")
    lastName = input("Enter your Last name: \n")
    email = input("Enter your email address: \n")
    password = input("Please create your password:\n")
    balance=input("please enter the amount you deposit:\n")
    accountNumber = generateAccountNumber()

    userDatabase[accountNumber] = [firstName, lastName, email, password, balance]
    # print("\n" , userDatabase.items())

    print("\nYour Account has been created successfully")

    print("**************Login details********************\n")
    print("Your account number is ", accountNumber)
    print("Make sure to keep it safe\n")
    print("************************************************\n")

    choice = input("Would you like to login to your account?(y/n)\n")
    if (choice == 'y'):
        login()
    else:
        init()



def login():
    flag = 0
    x = datetime.datetime.now()

    accountNumberFromUser =input("\nWhat is your Account Number?\n")

    isValidAccountNumber = accountNumberValidation(accountNumberFromUser)


    if isValidAccountNumber:

        password = input("\nWhat is your password?\n")

        for accountNumber, userDetails in userDatabase.items():
            if (accountNumber == int(accountNumberFromUser) and userDetails[3] == password):
                flag = 1
                print("**************Login successful*************** @ ", x)
                bankOperation(userDetails)

        if (flag == 0):
            print("Invalid account or password")
            op = input("Would you like to continue y/n?\n")
            if (op == 'y'):
                login()
            else:
                print("Quit\n")
                exit()

    else:
        init()

def accountNumberValidation(acNumber):

    if acNumber:

        if len(str(acNumber)) == 10:

            try:
                int(acNumber)
                print(acNumber)
                return True

            except ValueError:
                print ( "Invalid Account Number, it must be integer")
                return False

            except TypeError:
                print ( "Invalid Account Type")
                return False
            except:
                print("Invalid entry")
                return False


        else:
            print("Account Number must be 10 digits\n")
            return False

    else:
        print("\nAccount Number is required and  cannot be blank")
        return False




# bank operations

def bankOperation(user):
    print("************** Welcome %s %s ****************\n" % (user[0], user[1]))

    selectedOption = int(input(" What would you like to do?\n Bank operations:\n 1. Withdrawal\n 2. Cash Deposit\n 3. logout Account \n 4. Exit Bank operations\n "))
    # while(selectedOption !=4):

    if (selectedOption == 1):
        #print("\nWithdrawal function")
        currentBalance=getBalance(user)
        #print(currentBalance)
        x=withdrawOperation(currentBalance)
        user[4]= x
        op = input("would you like another operation(y/n)")
        if (op == 'y'):
            bankOperation(user)
        else:
            exit()

    elif (selectedOption == 2):
        print("\nDeposit function")
        depositOperation()
        op = input("would you like another operation(y/n)")
        if (op == 'y'):
            bankOperation(user)
        else:
            exit()


    elif (selectedOption == 3):
        print("Logging OUT of your account!")
        init()

    elif (selectedOption == 4):
        print("Quit Bank Operations\n")
        exit()
    else:
        print("Invalid option")
        bankOperation(user)


def withdrawOperation(cbalance):
    Amount = int(input("How much do you want to withdraw?\n"))
    if(cbalance>=Amount):
        cbalance= cbalance-Amount
        print("Take your cash!!!")
        print("Current Balance in your Account is ", cbalance)
        return cbalance
    else:
        return " can't withdraw: low balance"


def depositOperation():
    Amount = int(input("How much do you want to deposit?\n"))
    print("cash deposited!!!")


def getBalance(user):
    balance=user[4]
    return balance

def generateAccountNumber():
    print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)


####ACTUAL BANKING SYSTEM######

init()
