#class
## intiialize with a starting amount
class Banking():
    current_balance = 0

    def __init__(self, name, current_balance, x):
        self.name = name
        self.current_balance = current_balance
        self.x = x
        print("User, {}, has an account with us with a total of ${}!".format(self.name, self.current_balance))

    #method to deposit
    def deposit(self):
        raspberry = (self.current_balance + self.x)
        print("{} have made a deposit of ${}! \n You're new balance is ${}." .format(self.name, self.x, raspberry))
        return (raspberry)

    #method to withdraw
    def withdraw(self):
        strawberry = (self.current_balance - self.x)
        if strawberry < 0:
            print("Error! {} will be charged an overdraw fee!".format(self.name))
        else:
            print("{} have made a withdrawal of ${}! \n You're new balance is ${}.".format(self.name, self.x, strawberry))
        return (strawberry)


    #static
    #@staticmethod
    def status(self):
        print("Your balance is {} ".format(self.current_balance))


#error message if overdraws

#create users, include their starting balance
bank_user1 = Banking(name="Persephone",current_balance=50, x=25)
bank_user1.deposit()

bank_user2 = Banking(name="Ariadne",current_balance=500, x=25)
bank_user2.withdraw()

bank_user3 = Banking(name="Hera", current_balance=100, x=225)
bank_user3.withdraw()


