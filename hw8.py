

"""
import Banking script from another file
"""

import Banking
from Banking import Banking

#instantiate two users



bank_user1 = Banking(name="Artemis",init_balance=50, x=25)
bank_user1.deposit()
print("\n")

bank_user2 = Banking(name="Persephone",init_balance=500, x=25)
bank_user2.withdraw()
print("\n")

bank_user3 = Banking(name="Athena", init_balance=100, x=225)
bank_user3.withdraw()
print("\n")

user_name = input("To open an account, please provide your name.")
user_init = int(input("Please provide a starting balance."))
user_selection = int(input("Please select 1. for deposit or 2. for withdrawal"))
user_change = int(input("How much money will you be transferring today?"))


bank_user4 = Banking(name=user_name, init_balance=user_init, x=user_change)
if user_selection == 1:
    bank_user4.deposit()
if user_selection == 2:
    bank_user4.withdraw()

