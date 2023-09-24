class BankAccount:
    def withdraw(self, amount):
        self.balance = self.balance - amount

if __name__ == '__main__':
    mrA = BankAccount()
    mrA.balance = 1000
    print("mrA ->",mrA.balance)

    mrB = BankAccount()
    mrB.balance = 2000
    mrB.withdraw(300)
    print("mrB ->",mrB.balance)