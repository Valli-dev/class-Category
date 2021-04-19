def accountNumberValidation(acNumber):

    if acNumber:

            try:
                if int(acNumber):
                    if len(str(acNumber)) == 10:
                        return True
                    else:
                        print("Account Number must be 10 digits")
                        return False
            except ValueError:
                return False

            except TypeError:

                return False
            except:

                return False

    else:
        print("\nAccount Number is required and  cannot be blank")
        return False


#accountNumberValidation(1234567890)