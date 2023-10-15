class BankAccount:

    def __init__(self, name, balance = 0):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        print("--- func @property name ---")
        return self._name

    @property
    def balance(self):
        return self._balance
    
    @name.setter
    def name(self, value):
        print("this is name setter method")
        self._name = value

    def withdraw(self, amount):
        if amount > 0 and self._balance > amount:
            self._balance = self._balance - amount

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount


if __name__ == '__main__':
    chakrit = BankAccount('Chakrit', 2000)

    print(chakrit.name)    

    chakrit.name = "C. Wacharopas"
    print(chakrit.name)  

    chakrit.balance = -99999
