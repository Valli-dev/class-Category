class Category:
    amount = 0

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self,amount):
        self.amount += amount
        print("your have successfully deposited {} in {} category".format(amount, self.category))
        print("current balance" ,self.amount)
        return

    def check_balance(self,amount):
        if amount > self.amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.check_balance(amount):
            self.amount -= amount
            print("Balance after withdrawal= {}".format(self.amount) )
        else:
            print("can't withdraw: low balance")
        return

    def transfer(self, amount, category):
        if self.check_balance(amount):
            self.amount -= amount
            category.amount += amount
            print("Amount transferred successfully from {} object to {} object".format(self.category, category.category))
            print("New balance", category.amount)
        else:
            print("Amount can't be transfered")

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
amount= int(input("How much do you want to deposit to clothing category?\n"))
clothing_category.deposit(amount)
print("************* Withdraw operation***********")
w= int(input("How much do you want to withdraw from food category?\n"))
food_category.withdraw(w)

print("**************transfer operation between objects***************")
carexpense_category.transfer(50,education_category)




