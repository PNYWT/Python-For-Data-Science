
from datetime import datetime, timedelta
import pytz

# Model
class CardItem:
    def __init__(self,amount,type, exp=None) -> None:
        self.amount = int(amount)
        self.type = str(type)
        if exp == None:
            current_date = datetime.now()
            local_timezone = pytz.timezone('Asia/Bangkok')
            current_date = current_date.astimezone(local_timezone)
            seven_days = timedelta(days=7)
            self.dateExp = current_date + seven_days
        else:
            current_date = datetime.now()
            seven_days = timedelta(days=exp)
            self.dateExp = current_date + seven_days

    def topupMoenyFreeDays(self):
        self.dateExp += timedelta(days=7)

    def topupDate(self, exp):
        self.dateExp += timedelta(days=exp)
    
    def __str__(self):
        return '{0}, {1}'.format(self.amount, self.type)
    

# Class Function
class CashCard:

    def __init__(self, value, type, exp=None) -> None:
        self._typeCards = []
        setNameCard = "{0} CashCard".format(type)
        item = CardItem(value, setNameCard, exp)
        self._typeCards.append(item)
        self._value = int(value)
        self._type = type
        self._exp = item.dateExp

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if int(value) > 0:
            self._value = int(value)

    @property
    def type(self):
        return self._type
    
    @property
    def exp(self):
        return self._exp
    
    @property
    def typeCards(self):
        return self._typeCards
    
    def pay(self, amount):
        if (self._value - amount) > 0:
            self._value -= amount
        else:
            print("เงินไม่พอสำหรับใช้จ่าย")

    #add_cash
    def add_cash(self, amount): #เติม >= 500 เอาไปเลย 7 วัน
        if amount > 0:
            self._value += amount
            if amount >= 500:
                for card in self.typeCards:
                    if card.type == self.type:
                        card.topupMoenyFreeDays()
                        self._exp = card.dateExp
        else:
            print("กรุณากรอกจำนวนเงินใหม่อีกครั้ง")

    #openNewCard
    def openNewCard(self, value, type, exp=None):
        if value > 0:
            setNameCard = "{0} CashCard".format(type)
            item = CardItem(value, setNameCard, exp)
            self.typeCards.append(item)
            self._value = int(value)
            self._type = setNameCard
            self._exp = item.dateExp
            print("เปิดบัตรใหม่สำเร็จ สามารถเริ่มใช้บัตร {0} ได้เลย ยอดเงินปัจจุบัน {1} บาท วันหมดอายุ {2}".format(self.type, self.value, self.exp))
        else:
            print("เปิดบัตรใหม่ขั้นต่ำ 1 บาท")

    #changeCard
    def changeCard(self, type):
        setNameCard = "{0} CashCard".format(type)
        for card in self.typeCards:
            if card.type == str(setNameCard):
                self._value = card.amount
                self._type = card.type
                self._exp = card.dateExp
        print("ตอนนี้คุณใช้ {0} จำนวนเงินคงเหลือ {1} บาท วันหมดอายุ {2}".format(self.type, self.value, self.exp))

    def __str__(self) -> str:
        return "{0} {1} exp {2}".format(self.value, self.type, self.exp)

    

if __name__ == "__main__":
    cc1 = CashCard(20, "Science Food Court")
    print(cc1.value)
    cc1.pay(5)
    print(cc1.value)
    cc1.add_cash(10)
    print(cc1.value)
    cc1.openNewCard(100, "MaxValue")
    print(cc1)
    cc1.changeCard("Science Food Court")
    print(cc1)
    cc1.add_cash(500)
    print(cc1)
    cc1.openNewCard(500, "MRT", 15)
    print(cc1)




