# Assignment 23 Program 3

class BankAccount:
    ROI=105

    def __init__(self,Name,Amt):
        self.Name=Name
        self.Amount=Amt

    def Display(self):
        print("Account Holder Name :",self.Name)
        print("Current Balance is  :",self.Amount)
    
    def Deposit(self):
        Deposite=0
        print("Enter Amount to be Deposite :")
        Deposite=int(input())
        Deposite=Deposite+self.Amount
        self.Amount=Deposite
        return Deposite
    
    def Withdraw(self):
        Withdraw=0
        print("Enter Amount to be Withdraw :")
        Withdraw=int(input())
        if Withdraw<=self.Amount:
            Withdraw=self.Amount-Withdraw
            self.Amount=Withdraw
            return Withdraw
        else:
            print("Insufficient Balance ")
    
    def CalculateInterest(self):
        Interest=0
        Interest=(self.Amount*BankAccount.ROI)/100
        return Interest

Bobj1=BankAccount("A.B Roy",1000)
Bobj2=BankAccount("S.S Patil",3000)

print("----------Account Holder Details------------")
Bobj1.Display()
print("Amount After Deposited :",Bobj1.Deposit())
print("Amount after Withdraw  :",Bobj1.Withdraw())
print("Interest for amount is :",Bobj1.CalculateInterest())

print("----------Account Holder Details------------")
Bobj2.Display()
print("Amount After Deposited :",Bobj2.Deposit())
print("Amount after Withdraw  :",Bobj2.Withdraw())
print("Interest for amount is :",Bobj2.CalculateInterest())