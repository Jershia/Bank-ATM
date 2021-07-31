class ATM(object):
    def __init__(self,number,pin):
        self.number = number
        self.pin = pin
        
    def CashWithdrawl (self,takenAmount):
        amount = 85990 - takenAmount
        print("Your Balance Amount is " + str(amount))

    def BalanceEnquiry(self):
        print("Your Balance Amount is 85990")

def main():
        card = input("Enter your card number :")
        pin = input("Enter your pin :")
        user = ATM(card,pin)
        print("Enter 'b' for Balance enquiry and 'c' for Cash Withdrawl")
        choose = input("Enter your choice :")
        if(choose == "b"):
            user.BalanceEnquiry()
        elif(choose == "c"):
            takenAmount = int(input("Enter the amount :"))
            user.CashWithdrawl(takenAmount)
        else:
            print("Not Valid")

name = 0
if(name == 0):
    main()
