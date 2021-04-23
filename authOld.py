#login
  #(username or email) , password

#register
  # username , email, password
  # generate accountnumber

#bank operations

## Initialze the system


import random
database= {}

def init():
    isValidOption= False
    validList=[1,2]
    print("******************* WELCOME TO BANK PHP **********************")

    while(isValidOption==False):
        haveaccount= int(input("Do you have account with us? 1 (Yes) 2 (No)\n"))
        if (haveaccount == 1):
            isValidOption = True
            login()
        elif(haveaccount ==2):
            isValidOption = True
            register()
        elif(haveaccount not in validList):
            print("please enter valid option")

def register():
    print("********* New User Registration: ********** \n")
    
    firstName = input("Enter your first name: \n")
    lastName = input("Enter your Last name: \n")
    email = input("Enter your email address: \n")
    password = input("Please create your password:\n")
    accountNumber = generateAccountNumber()

    database[accountNumber]=[firstName, lastName, email, password]
    #print(database)
    print("Your Account has been created successfully")

    print("**************Login details********************\n")
    print("Your account number is ",accountNumber)
    print("Make sure to keep it safe\n")
    print("************************************************\n")

    print("Login to your Account\n")
    login()

def login():
    print("\nThis is the login function\n")
    isLoginSuccessful=False
    while (isLoginSuccessful== False):
        accountNumberFromUser = int(input("\nWhat is your Account Number?\n"))
        password = input("\nWhat is your password?\n")

        for accountNumber,userDetails in database.items():
            if (accountNumber==accountNumberFromUser and userDetails[3]==password):
                isLoginSuccessful=True
                print("**************Login successful***************")
                bankOperation(userDetails)
            else:
                print("invalid account or password, Try again")
        
def bankOperation(user):

    print("Welcome to Bank Operations %s %s" %(user[0], user[1]))
    selectedOption= int(input(" What would you like to do?\n Bank operations:\n 1. Withdrawal\n 2. Deposit\n 3. logout\n 4. Exit Bank operations\n "))
    if (selectedOption == 1):
        print("withdrawal function")
        withdrawOperation()
        
    elif(selectedOption == 2):
        print("deposit function")
        depositOperation()

    elif(selectedOption == 3):
        login()
    elif (selectedOption ==4):
        print("Quit Bank Operations\n")
        exit()
    else:
        print("Invalid option")
        bankOperation( user)





def withdrawOperation():
    print("How much do you want to withdraw?\n")

def depositOperation():
    print("How much do you want to deposit?\n")



def generateAccountNumber():
    print("Generating Account Number")
    return random.randrange(1111111111,9999999999)
    



####ACTUAL BANKING SYSTEM######

init()
#generateAccountNumber()



