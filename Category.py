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

    def transfer(self, amount, x):
        x.amount += amount
        print("Amount transfered successfully from {} to {}".format(self.category, x.category))


    def publish_categories(self):
        print( self.category,"\t\t" , "\t\t\t",self.amount)


print("AVAILABLE CATEGORIES AND THEIR BALANCES:\n")

#*********Object Instantiation***************#

clothing_category = Category("clothing", 1000)

clothing_category.publish_categories()
food_category = Category("food", 2000)
food_category.publish_categories()
entertainment_category = Category("Entertainment", 500)
entertainment_category.publish_categories()
carexpense_category = Category("CarExpenses", 1500)
carexpense_category.publish_categories()
education_category =Category("Education", 2500)
education_category.publish_categories()
print("************* Deposit operation***********")
d= int(input("How much do you want to deposit to clothing category?\n"))
clothing_category.deposit(d)

w= int(input("How much do you want to withdraw from food category?\n"))
food_category.withdraw(w)

#**************transfer operation between objects***************#


if carexpense_category. amount > 1000:
    print("car expense must be less than 1000")
    carexpense_category.transfer((carexpense_category.amount - 1000),education_category)
elif carexpense_category. amount < 900:
    carexpense_category.amount += 100


