class BankAccount:

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance = self.balance - amount

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def __str__(self):
        return "{0}'s balance = {1}".format(self.name, self.balance)

class SavingsAccount:

    def __init__(self, name, balance = 0, interest = 0.02):
        self.name = name
        self.balance = balance
        self.interest = interest

    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance = self.balance - amount

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def add_interest(self):
        self.balance += self.balance * self.interest

    def __str__(self):
        return "{0}'s balance = {1}".format(self.name, self.balance)


class SuperSavingsAccount:

    def __init__(self, name, balance = 0, interest = 0.02):
        self.name = name
        self.balance = balance
        self.interest = interest
        self.num_withdrawn = 0


    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            fee = 0
            self.num_withdrawn += 1
            if self.num_withdrawn >= 3:
                fee = 5
            self.balance = self.balance - amount - fee

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def add_interest(self):
        self.balance += self.balance * self.interest

    def __str__(self):
        return "{0}'s balance = {1}".format(self.name, self.balance)

normalAccount = BankAccount("Normal", 1000)
normalAccount.deposit(100)
print(normalAccount)

savings = SavingsAccount("Savings", 1000, 0.02)
savings.add_interest()
print(savings)

sup = SuperSavingsAccount("Super", 1000)
sup.withdraw(100)
sup.withdraw(100)
sup.withdraw(100)
print(sup)
