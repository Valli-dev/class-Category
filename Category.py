class Category:
    amount = 0

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self,amount):
        self.amount += amount
        print("your have successfully deposited {} in {} category".format(amount, self.category))
        self.check_balance()
        return

    def check_balance(self):
        print ("Current balance : {} in {} category".format(self.amount, self.category))
        return True

    def withdraw(self, amount):

        if (amount > self.check_balance()):
            self.amount -= amount
            print("Balance after withdrawal= {}".format(self.amount) )
        else:
            print("can't withdraw: low balance")
        return

    def transfer(self, amount, obj):
    
        if self.amount > 100:
            print("car expense must be less than 100")
            x=self.amount -100
            self.amount=self.amount-100
            obj.amount += x
            print("current balance at carexpense :", self.amount)
            print("New balance at {} : {} ".format(obj.category, obj.amount))
            print("Amount transferred successfully from {} object to {} object".format(self.category, obj.category))
            
        elif self.amount < 90:
            self.amount += 10
            print("carexpense_category amount updated ")
            return


    def publish_categories(self):
        print( self.category,"\t\t" , "\t\t\t",self.amount)


print("AVAILABLE CATEGORIES AND THEIR BALANCES:\n")

#*********Object Instantiation***************#

clothing_category = Category("clothing", 100)

clothing_category.publish_categories()
food_category = Category("food", 200)
food_category.publish_categories()
entertainment_category = Category("Entertainment", 50)
entertainment_category.publish_categories()
carexpense_category = Category("CarExpenses", 150)
carexpense_category.publish_categories()
education_category =Category("Education", 250)
education_category.publish_categories()
print("************* Deposit operation***********")
d= int(input("How much do you want to deposit to clothing category?\n"))
clothing_category.deposit(d)
print("************* Withdraw operation***********")
w= int(input("How much do you want to withdraw from food category?\n"))
food_category.withdraw(w)

print("**************transfer operation between objects***************")
carexpense_category.transfer(carexpense_category,education_category)

