class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


class SavingsAccount(Account):
    def calculate_interest(self, interest_rate):
        if interest_rate > 0:
            interest = self.balance * (interest_rate / 100)
            self.balance += interest
            return self.balance
        else:
            return self.balance


class CheckingAccount(Account):
    def check_acc(self):
        return self.balance


savings_account = SavingsAccount("George", 1000)
print(savings_account.deposit(500))
print(savings_account.calculate_interest(2))
print(savings_account.withdraw(200))

checking_account = CheckingAccount("Cristian", 800)
print(checking_account.deposit(300))
print(checking_account.withdraw(1000))
