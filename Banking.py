#!usr/bin/env Python 3

"""
This script will execute a banking module for Goddess Online Credit Union

To run this script from the command line type
Banking.py

Assumptions:
this script should be used as a module for other python scripts

Requires:
Anaconda Python3
"""


## intiialize with a starting amount
class Banking():
    balance = 0

    def __init__(self, name, init_balance, x):
        self.name = name
        self.init_balance = init_balance
        self.x = x
        # print("User, {}, has an account with us with an initial balance of ${}!".format(self.name, self.init_balance))

    #method to deposit
    def deposit(self):
        # current_balance = (self.init_balance + self.x)
        balance = self.init_balance + self.x
        #print(balance)
        print("Okay!")
        return (balance)

    #method to withdraw
    def withdraw(self):
        balance = (self.init_balance - self.x)
        #overdraw error message
        if balance < 0:
            print("Error! {} will be charged an overdraw fee!".format(self.name))
        else:
            print("Okay!")
        return (balance)


    #static
    #@staticmethod
    def status(self):
        print("Goddesses balance is {} ".format(self.current_balance))



#dummy data to test class features
"""
#bank_user1 = Banking(name="Persephone",init_balance=50, x=25)
#bank_user1.deposit()

#bank_user2 = Banking(name="Ariadne",init_balance=500, x=25)
#bank_user2.withdraw()

#bank_user3 = Banking(name="Hera", init_balance=100, x=225)
#bank_user3.withdraw()
"""




#bank_user2 = Banking(name="Ariadne",init_balance=500, x=25)
#bank_user2.withdraw()

#bank_user3 = Banking(name="Hera", init_balance=100, x=225)
#bank_user3.withdraw()
"""


