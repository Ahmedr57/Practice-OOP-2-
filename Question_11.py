# Create a base class BankAccount with methods deposit() and withdraw(). 
# Derive two classes SavingsAccount and CheckingAccount with different interest rates. 
# Implement a method apply_interest() in each derived class that calculates interest differently. 
# Demonstrate polymorphism by writing a function that accepts any account type and applies interest.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount Withdrawn: {amount}")
        else:
            print("Insufficient funds") 

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class CheckingAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 12
        self.balance += interest

class AccountManager:
    def __init__(self):
        pass
    def apply_interest_to_account(self, account):
        account.apply_interest()



account_manager = AccountManager()

# Using accountmanger for saving account.
savings_account = SavingsAccount(1000, 0.05)
account_manager.apply_interest_to_account(savings_account)        
print("Savings account balance:", savings_account.balance)

# Using accountmanger for chechking account
checking_account = CheckingAccount(500, 0.01)
account_manager.apply_interest_to_account(checking_account)
print("Checking account balance:", checking_account.balance)
