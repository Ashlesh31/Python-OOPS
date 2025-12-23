import random
class Account:
    account_no = 9834128733
    def __init__(self, name, age, mobileno, pin):
        self.name = name
        self.age = age
        self.mobileno = mobileno
        self.accno = Account.account_no
        Account.account_no += 1
        self.ifsc = self.generate_ifsc()
        self.bal = 0
        self.card = self.create_ATM_card(pin)
    
    def generate_ifsc(self):
        bank_code = 'SBIN'
        branch_code = random.randint(1000, 9999)
        return bank_code + str(branch_code)
    
    def create_ATM_card(self, pin):
        card_no = int(random.randint(111111111111, 999999999999))
        return ATMcard(card_no, pin)
    
    def modify_balance(self, amount):
        self.bal += amount


class ATMcard:
    def __init__(self, cardno, pin):
        self.cardno = cardno
        self.__pin = pin

    def verify_card(self, entered_pin):
        return self.__pin == entered_pin

class ATM:
    def __init__(self):
        self.current_account = None
    def insert_card(self, acc):
        self.current_account = acc
        print('Card inserted')
    def withdraw(self):
        pincode = self.checkPin()
        if self.authenticate(pincode):
            amount = int(input("enter the amount to withdraw between 500 to 10000: "))
            if amount <= self.current_account.bal:
                if 500 <= amount <= 10000:
                    self.current_account.modify_balance(-amount)
                    print('Amount debited')
                    print(f'Available balance is {self.current_account.bal}')
                else:
                    print("proper amount")
            else:
                print('insufficient amount')
        else:
            print('Wrong pin')
    def deposit(self):
        pincode = self.checkPin()
        if self.authenticate(pincode):
            amount = int(input('Enter the amount you want to deposit: '))
            if amount > 0:
                self.current_account.modify_balance(amount)
                print(self.current_account.bal)
            else:
                print('Enter proper amount')
        else:
            print('Invalid card number')

    def authenticate(self, pin):
        if self.current_account.card.verify_card(pin):
            print('Card verified')
            return True
        print('Wrong pin')
        return False

    @staticmethod
    def checkPin():
        pin = int(input("Enter the 4 digit pin: "))
        return pin



a1 = Account('ashlesh', 22, 8088176169, 2003)
a2 = Account('rathan', 22, 3121234567, 3002)
a3 = Account('Akhilesh', 22, 8088715267, 2222)
atm = ATM()
atm.insert_card(a3)
atm.deposit()
atm.withdraw()