

"""
import Banking script from another file
"""

import Banking
from Banking import Banking

#instantiate two users

print("Welcome user Artemis! Your initial balance is $50")
selection = int(input("Select 1. for deposit or 2. for withdraw"))
raspberry = int(input("How much would you like to deposit/withdraw"))

bank_user1 = Banking(name="Artemis", init_balance=50, x=raspberry)

if selection == 1:
bank_user1.deposit()
if selection ==2:
bank_user2.withdraw()
print("\n")


print("Welcome user Persephone. You'r initial amount is $5000")
selection = int(input("Select 1. for deposit or 2. for withdraw"))
mango = int(input("How much would you like to deposit/withdraw"))
bank_user2 = Banking(name="Persephone", init_balance=5000, x=mango)

if selection == 1:
    bank_user2.deposit()
if selection == 2:
    bank_user2.withdraw()

print("\n")

print("testing error message")
bank_user3 = Banking(name="Athena", init_balance=100, x=225)
bank_user3.withdraw()
print("\n")
