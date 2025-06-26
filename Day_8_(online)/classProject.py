from abc import ABC, abstractmethod

#Base Class

class BankAccount(ABC):
    def __init__(self, owner, balance = 0, interest_rate =0):
        self.owner = owner
        self.__balance = balance # private attribute
        self.__interesst_rate = interest_rate #private attribute

    @property
    def balence(self): #Getter
        return self.__balance

    @balence.setter
    def balance(self, amount): # setter
        if amount < 0:
            print('Balance cannot be negative!')
        else:
            self.__balance = amount

    @property
    def interest(self): #Getter
        interest = self.balence * self.__interest_rate
        return interest

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'\n Deposited ${amount}. Current balance $${self.balance}')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balence:
            self.__balance -= amount
            print(f'\nWithdrew $ {amount}. Current balance ${self.balance}')

    @abstractmethod # is required to use in the sub classes
    def display_account_details():
        pass

#creating subclasses

class SavingAccount(BankAccount):
    def __init__(self, owner, balance = 0)
        super.__init__(owner, balance, 0.05)

    def display_account_details(self):
        pass

class CheckingAccount(BankAccount):
    def __
    

# Creating objects

paula = BankAccount('Paula', 2000, 2)
print.deposit(2000)
print.withdraw(100)




#below this line, all of Paula's code:

from abc import ABC, abstractmethod

# Base class

class BankAccount(ABC):
    def __init__(self, owner, balance = 0, interest_rate = 0):
        self.owner = owner
        self.__balance = balance # Private attribute
        self.__interest_rate = interest_rate # Private attribute

    @property
    def balance(self): #Getter
        return self.__balance
    
    @balance.setter
    def balance(self, amount): # Setter
        if amount < 0:
            print('Balance can`t be negative')
        else:
            self.__balance = amount

    @property
    def interest_income(self): # Getter
        interest_income = self.balance * self.__interest_rate
        return interest_income
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'\nDeposited 💲{amount}. Current balance 💲{self.balance}')
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f'\nWithdrew 💲 {amount}. Current balance 💲{self.balance}')
        else:
            print('You don`t have enough money 😭')
    
    @abstractmethod # Is required to use in the sub classes
    def display_account_details(self):
        pass

# Creating subclasses

class SavingAccount(BankAccount):
    def __init__(self, owner, balance = 0):
        super().__init__(owner, balance, 0.05)
    
    def display_account_details(self):
        print('\n=========== 🏦 ===============')
        print('SAVINGS ACCOUNT')
        print(f'Account owner: {self.owner}')
        print(f'Balance 💲 {self.balance}')
        print(f'Interest 🧩 {self.interest_income}')
        print('=============================')

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance = 0):
        super().__init__(owner, balance)
    
    def display_account_details(self):
        print('\n=========== 🏦 ===============')
        print('CHECKING ACCOUNT')
        print(f'Account owner: {self.owner}')
        print(f'Balance 💲 {self.balance}')
        print('=============================')

# Creating objects

# paula = BankAccount('Paula', 2000, 2)
# paula.deposit(2000)
# paula.withdraw(100)

paula = SavingAccount('Paula', 2000)
paula.display_account_details()
paula.deposit(40000)
paula.display_account_details()
paula.withdraw(2000)
paula.display_account_details()

sam = CheckingAccount('Sam', 1500)
sam.display_account_details()
sam.deposit(90)
sam.display_account_details()
sam.withdraw(4000)
sam.display_account_details()

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

def main():

    savings_account = SavingAccount("Paula", 100)

    checking_account = CheckingAccount("Paula", 200)

    accounts = [savings_account, checking_account]

    print(f"\n 🏦 Welcome to the {GREEN}Bank{RESET} system! Choose an option:")

    while True:
        print('\033[32m') #Change green color to the content
        savings_account.display_account_details()
        checking_account.display_account_details()
        
        print('\033[0m') #Change white color to the content
        print(f"1️⃣ Deposit money")
        print(f"2️⃣ Withdraw money")
        print(f"3️⃣ Exit")

        choice = int(input("\nEnter your choice (1,2): "))

        if choice == 3:
            break
        
        print(f"1️⃣ Savings Account")
        print(f"2️⃣ Checking Account")
        account_choice = int(input("\nEnter your choice (1,2): "))

        amount_choice = int(input("How much!!🤑, enter the amount: "))

        if choice == 1:
            accounts[account_choice-1].deposit(amount_choice)
        else:
            accounts[account_choice-1].withdraw(amount_choice)

    print("Have a Good day 😊")

main() 
