import random


class atm:
    def enterInfo(PIN, AtmNumber):
        chooseMethod = input("Enter 1 for Cash Withdrawal and 2 for Balance Enquiry")
        if chooseMethod == 1:
            print("Cash Withdrawal is currently under maintenance. Sorry for inconvenience")
        if chooseMethod == 2:
            print("Balance Enquiry is currently under maintenance. Sorry for inconvenience")

