class BankAccount:

    def __init__(self, name, balance = 0) -> None:
        self._name = name
        self._balance = balance #private เสมือน

    @property
    def name(self):
        return self._name
    
    @name.setter
    def newName(self, newName):
        print(self.name, "change to", newName)
        self._name = newName

    @property
    def balance(self):
        print("This is property Balance")
        return self._balance
    
    def withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self._balance = self._balance - amount

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount

if __name__ == '__main__': #เขียนทดสอบเฉยๆ จำลองการเขียนใช้จริง
    mrA = BankAccount("MR.A", 1000)
    mrB = BankAccount("MR.B", 2000)

    mrA.withdraw(300)
    print("mrA.withdraw ->", mrA.balance) #เรียก @property def balance

    mrB.withdraw(500)
    print("mrB.withdraw ->", mrB.balance)

    # mrB.balance = 1000000 ไม่สามารถ Run ได้เพราะมีการปกป้องตัวแปรด้วย @property และไม่มี setter จึงระบุค่าใหม่ไม่ได้

    mrB.newName = "MR.BB" #เรียก @name.setter def newName
    print("mrB change name to ->", mrB.name) #เรียก @property def name