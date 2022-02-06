import random

class Atm(object):
    def __init__( self, accountNumber, accountPassword, moneyInAccount):
        self.accountNumber = accountNumber 
        self.accountPassword = accountPassword 
        self.moneyInAccount = moneyInAccount

    def MoneyTransaction( self, moneyToTakeOut):
        if self.moneyInAccount > moneyToTakeOut :
            self.moneyInAccount = self.moneyInAccount - moneyToTakeOut
            print("Succesfully Transacted Ruppess "+str( moneyToTakeOut))
        else:
            print("You Dont Have Enough Money in your Account")
            print("Current Balance : "+ str(self.moneyInAccount))
    
    def BankEnquiry( self):
        print("Account Number : "+ str(self.accountNumber))
        print("Current Balance : ₹"+ str(self.moneyInAccount))

print("Welcome to White Hat jr Bank")

accountNumber = input("Enter your Account Number : ")
accountPassword = input("Enter your Accunt Password : ")
moneyInAccount = int(random.random() * (100 - 1) + 1) * 1000

atm = Atm(accountNumber, accountPassword, moneyInAccount)

print("what would you like to do today")
print("Enter 1 for Money Transaction")
print("Enter 2 for Bank Enquiry")

response = int(input("Enter : "))

if response == 1:
    moneyToTakeOut = int(input("How much would you like to WithDraw : "))
    atm.MoneyTransaction(moneyToTakeOut)

if response == 2:
    atm.BankEnquiry()

while response <= 0 or response >= 3:
    print("Enter a number between 1 and 2")
    response = int(input("Enter : "))