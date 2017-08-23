#!usr/bin/env Python 3

"""
This script will execute a banking module for Goddess Online Credit Union

To run this script from the command line type
python hw8.py

Assumptions:


Requires:
Anaconda Python3
Banking
"""

import Banking
from Banking import Banking

#instantiate two users

goddesses = ["Artemis", "Persephone"]

print("Welcome to Goddess Online Credit Union (Please note, goddesses do not use change. They only use integers)")
print("The following goddesses have already opened accounts: {}".format(goddesses))
goddess = input("Please provide your goddess name to deposit or withdraw to your account.")


a_balance = 3500
p_balance = 5000
new_balance = 100

while goddess == "Artemis":
    print("\n")
    print("Welcome Artemis! Let me check your balance for you!")
    print("Your initial balance is ${}".format(a_balance))
    selection = int(input("Select 1. to deposit or 2. to withdraw 3. to exit"))
    if selection == 3:
        exit()

    raspberry = int(input("How much would you like to deposit/withdraw"))
    bank_user1 = Banking(name="Artemis", init_balance=a_balance, x=raspberry)

    if selection == 1:
        a_balance = bank_user1.deposit()
        print("Your current balance is: ${}".format(a_balance))
    #    print(balance)
    if selection ==2:
        a_balance = bank_user1.withdraw()
        print("Your current balance is: $ {}".format(a_balance))
    selection = ("Please make another selection. 1. to deposit 2. to withdraw 3. to exit")
    print("\n")



while goddess == "Persephone":
    print("Welcome Persephone! Let me check your balance for you!")
    print("You're initial balance is ${}".format(p_balance))
    selection = int(input("Select 1. to deposit or 2. to withdraw 3. to exit"))
    if selection == 3:
        exit()

    raspberry = int(input("How much would you like to deposit/withdraw"))
    bank_user2 = Banking(name="Persephone", init_balance=p_balance, x=raspberry)

    if selection == 1:
        p_balance = bank_user2.deposit()
        print("Your current balance is: $ {}".format(p_balance))
    if selection ==2:
        print("Your current balance is: ${}".format(p_balance))
        p_balance = bank_user2.withdraw()
    selection = int(input("Select 1. to deposit or 2. to withdraw 3. to exit"))
    print("\n")



while goddess != "Artemis" or "Persephone":
    print("Welcome Goddess {}".format(goddess))
    print("All new accounts start at $100")
    selection = int(input("Select 1. to deposit or 2. to withdraw 3. to exit"))
    if selection == 3:
        exit()
    raspberry = int(input("How much would you like to deposit/withdraw"))
    bank_user3 = Banking(name="goddess", init_balance=new_balance, x=raspberry)

    if selection == 1:
        new_balance = bank_user3.deposit()
        print("Your current balance is: ${}".format(new_balance))

    #    print(balance)
    if selection ==2:
        new_balance = bank_user3.withdraw()
        print("Your current balance is: ${}".format(new_balance))
