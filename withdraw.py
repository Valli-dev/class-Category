import database
import validation
from getpass import getpass
import os
import datetime

user_database_path = "data/user_record/"
user_authentication_path="data/auth_session/"


def withdraw(acNumber, amount ):
    all_users = os.listdir(user_database_path)
    try:

        for user in all_users:
            if (user == str(acNumber)+ ".txt"):
                with open(user_database_path + str(acNumber) + ".txt", "r") as f:
                        for line in f:

                            print(f.read())

                        last_line = line
                        print("I am last line" ,last_line)


    except FileNotFoundError:

        print("file not found")


    else:

            try:

                '''user_list = str.split(last_line, ',')
                newbal = int(user_list[2]) - amount
                user_list[2] = newbal
                updated_entry= str(user_list)
                f = open(user_database_path + str(acNumber) + ".txt", "a")'''

                user_list = str.split(last_line, ',')
                print(user_list)
                newbal = int(user_list[2]) - amount
                user_list[2] = newbal
                print(user_list[2])
                updated_entry = str(user_list)
                print(updated_entry)

            except:

                print("can't update file")

            else:
                f.write("\n\n")
                f.write( updated_entry)



            finally:
                f.close()







#withdraw(acNumber, amount)