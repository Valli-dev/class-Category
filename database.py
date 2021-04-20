import os
import validation
import datetime

user_database_path = "data/user_record/"
user_authentication_path="data/auth_session/"

def create(accountNumber,firstName, lastName, balance, password, email):


    userDetails = firstName + "," + lastName + "," +balance + "," + password + "," + email

    if does_account_exists(accountNumber):
        #print("Account already exists\n")
        return False

    if does_email_exists(email):
        #print("Email exists\n")
        return False


    file_created_flag = False

    try:
        print("New User record creation ")
        f = open("data/user_record/" + str(accountNumber) + ".txt", "x")

    except FileExistsError:

        print("file already exists")
        file_contents= read("data/user_record/" + str(accountNumber) + ".txt")
        if not file_contents:
            delete(accountNumber)

    else:
        f.write(userDetails)
        file_created_flag= True

    finally:
        f.close()

    return file_created_flag



def authentication(accountNumberFromUser, password):
    if does_account_exists(accountNumberFromUser):

        user= str.split(read(accountNumberFromUser), ',')

        if password == user[3]:

            return user
    else:
        return False



def auth_sessionlogin(accountNumberFromUser):

    print("Creating Login Entry in auth session file ")
    try:

        f = open("data/auth_session/" + str(accountNumberFromUser) + ".txt", "x")

    except FileExistsError:
        print("cant create file: already exists")

    else:
        x = datetime.datetime.now()
        with open("data/auth_session/" + str(accountNumberFromUser) + ".txt", "w") as f:

            f.write(" \n User Login entry recorded @ time %s:"  % datetime.datetime.now())
    return True



def auth_session_logout(accountNumberFromUser):

    deleteflag = False

    if os.path.exists(user_authentication_path+ str(accountNumberFromUser) + ".txt"):

        try:
            os.remove(user_authentication_path+ str(accountNumberFromUser) + ".txt")
            deleteflag = True

        except FileNotFoundError:
            print("User login session file not found to delete")


    return deleteflag


def withdraw(acNumber,amount, user):

    print(user)
    all_users = os.listdir(user_database_path)
    try:
        last_line = getbalance(acNumber)
        print(last_line)
        last_line_list = str.split(last_line, ',')
        print([last_line_list])
        if int(last_line_list[2]) > int (amount):

            newbal = int(last_line_list[2]) - int(amount)
            last_line_list[2] = str(newbal)
            update = str(last_line_list)
            print("Please take your amount\nyour current balance is ", newbal)

        else:

            print("low balance")


    except FileNotFoundError:

        print("file not found")

    except ValueError:
        print('cant add str with int')

    else:

            try:
                f = open(user_database_path + str(acNumber) + ".txt", "a")

            except:

                print("can't update file")

            else:
                f.write("\n")
                #firstName + "," + lastName + "," + balance + "," + password + "," + email
                updated_list = user[0]+ "," + user[1] + "," + str(newbal) + "," + user[3] + "," + user[4]
                f.write(updated_list)
                print("File Updated")


            finally:
                f.close()


    return True


def deposit(acNumber,amount,user):

    all_users = os.listdir(user_database_path)
    try:

        last_line= getbalance(acNumber)
        print(last_line)
        last_line_list = str.split(last_line,',')
        print(last_line_list)
        print(last_line_list[2])
        newbal = int(last_line_list[2]) + int(amount)

        last_line_list[2] = str(newbal)
        update = str(last_line_list)
        print("Your amount has been deposited successfully \nyour current balance is ", newbal)

    except FileNotFoundError:

        print("file not found")
    except ValueError:
        print("can't add str and int")


    else:

            try:
                f = open(user_database_path + str(acNumber) + ".txt", "a")

            except:

                print("can't update file")

            else:
                f.write("\n")
                updated_list = user[0] + "," + user[1] + "," + str(newbal) + "," + user[3] + "," + user[4]
                f.write(updated_list)
                print("File Updated")


            finally:
                f.close()


    return True



def getbalance(acNumber):
    all_users = os.listdir(user_database_path)
    try:

        for user in all_users:
            if (user == str(acNumber)+ ".txt"):
                with open(user_database_path + str(acNumber) + ".txt", "r") as f:
                        for line in f:
                            f.readline()
                        last_line = line
                #print("I am last line",last_line)
                #user_list = str.split(last_line, ',')
                #cbalance= user_list[2]

    except FileNotFoundError:

        print("file not found")

    return last_line








def read(acNumber):
    is_valid_account_number = validation.accountNumberValidation(acNumber)

    try:
        if (is_valid_account_number):

            f = open(user_database_path + str(acNumber) + ".txt", "r")

        else:
            f = open(user_database_path + acNumber, "r")

    except FileNotFoundError:
        print("file not found")

    except TypeError:
        print("Invalid account number format")

    else:
        return (f.readline())


    return False


# find user with acNumber
# delete the userfile
# return true


def delete(acNumber):
    print("delete user record")
    deleteflag = False
   # print("1")
    if os.path.exists(user_database_path + str(acNumber) + ".txt"):

        try:
            os.remove(user_database_path + str(acNumber) + ".txt")
            deleteflag = True


        except FileNotFoundError:
            print("User not found")

        finally:
            return deleteflag



def does_email_exists(email):

    all_users = os.listdir(user_database_path)

    for user in all_users:
        user_list= (str.split(read(user), ','))

        if email in user_list:
            print("email exists: ", email)
            return True

    return False




def does_account_exists(acNumber):

    all_users = os.listdir(user_database_path)
    for user in all_users:
        if user == str(acNumber) + ".txt" :
            #print("account Number exists", acNumber)
            return True
    else:

        #print("account Number does not exists")
        return False



#auth_session_logout(6985162718)
#authentication(8784717206, "pass")
#does_account_exists(8784717226)
#print(does_email_exists('seyyyi@gmail.com'))

#create(1703085570,['Seyi', 'Onifade', 'seyionifade@zuriteam.com', 'PasswordSeyi', 1000])
# delete(9971594670)
#print(read(())
#GFGFjhhg