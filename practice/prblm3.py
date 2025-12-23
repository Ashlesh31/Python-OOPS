class BankAccount():
    def __init__(self,account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        if self.account_number == int(input("enter the account number: ")):
            amount = int(input('enter the amount you want to deposit: '))
            if amount % 100 == 0:
                self.balance += amount
                return self.display_balance()
            else:
                print('enter proper denominations')
        else:
            print('invalid account number')
    def withdraw(self):
        if self.account_number == int(input("enter the account number: ")):
            amount = int(input("enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                return self.display_balance()
            else:
                print("insufficient amount")
        else:
            print('Invalid account number')
    def display_balance(self):
        return self.balance

karntBank = BankAccount(123456789, 50000)
print(karntBank.deposit())
print(karntBank.withdraw())