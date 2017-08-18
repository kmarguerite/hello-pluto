#class
## intiialize with a starting amount
class Banking():
    current_balance = 0

    def __init__(self, name, init_balance, x):
        self.name = name
        self.init_balance = init_balance
        self.x = x
        print("User, {}, has an account with us with an initial balance of ${}!".format(self.name, self.init_balance))

    #method to deposit
    def deposit(self):
        current_balance = (self.init_balance + self.x)
        print("{} has made a deposit of ${}! \n  The new balance is ${}." .format(self.name, self.x, current_balance))
        return (current_balance)

    #method to withdraw
    def withdraw(self):
        current_balance = (self.init_balance - self.x)
        #overdraw error message
        if current_balance < 0:
            print("Error! {} will be charged an overdraw fee!".format(self.name))
        else:
            print("{} has made a withdrawal of ${}! \n The new balance is ${}.".format(self.name, self.x, current_balance))
        return (current_balance)


    #static
    #@staticmethod
    def status(self):
        print("Your balance is {} ".format(self.current_balance))


#dummy data to test class features

"""
#bank_user1 = Banking(name="Persephone",init_balance=50, x=25)
#bank_user1.deposit()

#bank_user2 = Banking(name="Ariadne",init_balance=500, x=25)
#bank_user2.withdraw()

#bank_user3 = Banking(name="Hera", init_balance=100, x=225)
#bank_user3.withdraw()
"""


