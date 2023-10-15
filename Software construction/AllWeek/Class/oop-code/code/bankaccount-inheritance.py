class BankAccount:

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def __str__(self):
        return "{0}'s balance = {1}".format(self.name, self.balance)

class SavingsAccount(BankAccount):

    def __init__(self, name, balance = 0, interest = 0.02):
        super().__init__(name, balance)
        self.interest = interest

    def add_interest(self):
        self.balance += self.balance * self.interest

class SuperSavingsAccount(SavingsAccount):

    def __init__(self, name, balance = 0, interest = 0.02):
        super().__init__(name, balance, interest)
        self.num_withdrawn = 0

    ## override method
    def withdraw(self, amount):
        fee = 0
        self.num_withdrawn += 1
        if self.num_withdrawn >= 3:
            fee = 5
        # self.balance = self.balance -(amount + fee)
        super().withdraw(amount + fee)  ## good practice : 
                                        ##   reuse code from superclass


if __name__ == '__main__':

    savings_act = SavingsAccount("Tom", 600, 0.03)

    ### ได้รับ variable จาก superclass
    print(savings_act.name)
    print(savings_act.balance)

    ### ได้รับ method จาก superclass
    savings_act.deposit(400)
    print(savings_act.balance)

    ### เพิ่ม method ของตนเองได้
    savings_act.add_interest()
    print(savings_act.balance)

    ### ปรับแต่งหรือ override method ของ superclass ได้
    super_savings = SuperSavingsAccount("Cecila", 1000, 0.03)
    super_savings.withdraw(100)
    super_savings.withdraw(100)
    super_savings.withdraw(100)
    print(super_savings)



