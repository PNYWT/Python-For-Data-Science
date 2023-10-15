class BankPublic:
    def __init__(self, name, balance=0) -> None:
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def __str__(self) -> str:
        return "{0}'s balance = {1}".format(self.name, self.balance)

class SavingsAccount(BankPublic): # SubClass of BankPublic
    def __init__(self, name, balance = 0, interest = 0.02) -> None:
        super().__init__(name, balance)
        self.interest = interest

    def add_interest(self):
        self.balance += self.balance * self.interest

class SuperSavingsAccount(SavingsAccount): # Derived class of SuperSavingsAccount
        
    def __init__(self, name, balance = 0, interest=0.02) -> None:
        super().__init__(name, balance, interest)
        self.num_withdrawn = 0

    ## override method
    def withdraw(self, amount):
        self.fee = 0
        self.num_withdrawn += 1
        if self.num_withdrawn >= 3:
            self.fee = 5
        # self.balance = self.balance - amount - fee
        super().withdraw(amount + self.fee) # เรียก withdraw ของ BankPublic

savings_act = SavingsAccount("Tom", 600, 0.03)
print(savings_act.name) #เรียก name ของ BankPublic
print(savings_act.balance) #เรียก balance ของ BankPublic

savings_act.deposit(400) #เรียก deposit ของ BankPublic
print(savings_act.balance)

savings_act.add_interest() #เรียก deposit ของ ตัวเอง
print(savings_act.balance) #เรียก deposit ของ BankPublic
print("---------------")
savings_act2 = SuperSavingsAccount("Tony", 1000, 0.05)
print(savings_act2.name) #เรียก name ของ SavingsAccount
print(savings_act2.balance) #เรียก balance ของ SavingsAccount

savings_act2.deposit(400) #เรียก deposit ของ BankPublic
print(savings_act2.balance)

savings_act2.withdraw(100) #เรียก withdraw ของ ตัวเอง
print(savings_act2.num_withdrawn) #เรียก num_withdrawn ของ ตัวเอง
savings_act2.withdraw(100) #เรียก withdraw ของ ตัวเอง
print(savings_act2.num_withdrawn) #เรียก num_withdrawn ของ ตัวเอง
print(savings_act2.fee) #เรียก fee ของ ตัวเอง
savings_act2.withdraw(100) #เรียก withdraw ของ ตัวเอง
print(savings_act2.num_withdrawn) #เรียก num_withdrawn ของ ตัวเอง
print(savings_act2.balance) #เรียก deposit ของ BankPublic
print(savings_act2.fee) #เรียก fee ของ ตัวเอง