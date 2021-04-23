from datetime import datetime
name = input("Enter your name:")
userlist=['Seyi','Mike','Valli','John']
passwordlist=['PasswordSeyi','PasswordMike','PasswordValli','PasswordJohn']
if (name in userlist):
    userid=userlist.index(name)
    
    password= input("please enter the password: ")
    if (password == passwordlist[userid]):
        print("\nWelcome %s !!!!!!!!\n" % name)

        now = datetime.now()
        #d1= day.strftime("%B-%d-%Y")
        print("login date and time = ", now)

        Boolean= True
        balance=100
        while(Boolean): 
            print("\nWhat do you want to do?\n 1. Withdrawal \n 2. Cash deposit\n 3. Complaint\n")
        
            selectedoption= int(input("Please enter an option:"))
            if(selectedoption==1):
                print("\n-------Withdrawal--------")
            
                a=int(input("How much money would you like to withdraw?"))
                print("Take your  ${0} cash !!! ".format(a))
                
            
            elif(selectedoption==2):
                print("\n------Cash Deposit--------")
                deposit=int(input("How much money you want to deposit?"))
                AcBalance= balance + deposit
                print("Amount deposited\n Available balance = $", AcBalance)
                
            elif(selectedoption==3):
                print("-------Make Complaint--------")
                complaint= input("What issue would you like to report? ")
                print("\nYOUR COMPLAINT ON :\n\n" ,complaint) 
                print("complaint registered.\nThank you for contacting us\n") 
            else:
                print("Invalid option, please try again")
                Boolean= False
           
    else:
        print("Password incorrect, please try again")
        
else:
    print("User Name not found, please try again")
