# class Student:
#     def __init__(self,name,year) -> None:
#         self.name = name
#         self.year = year

#     def advance(self):
#         self.year += 1

# if __name__ == '__main__':
#     kwan = Student('Kwan', 2)
#     jaidee = Student('Jaidee', 1)
#     print(kwan.name)
#     print(jaidee.name)

#     kwan.advance()
#     jaidee.advance()

#     print(kwan.year)
#     print(jaidee.year)

# class Rectangle:
#     def __init__(self,x,y,w,h):
#         self.pos = (x,y)
#         self.width = w
#         self.height = h

#     def area(self):
#         return self.width * self.height


# import math
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2
    
#     def circumference(self):
#         return 2*math.pi*self.radius
    
# if __name__ == "__main__":
#     c1 = Circle(5)
#     c2 = Circle(8)

#     print(c1.radius)
#     print(c2.radius)
#     print("%.2f" %c1.area())
#     print("%.2f" %c2.area())
#     print("%.2f" %c1.circumference())
#     print("%.2f" %c2.circumference())

# import math
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def bigger_than(self, radiusOther):
#         return self.radius > radiusOther.radius

# if __name__ == "__main__":
#     c1 = Circle(12)
#     c2 = Circle(10)
#     print(c1.bigger_than(c2))

#     c3 = Circle(30)
#     c4 = Circle(45)
#     print(c3.bigger_than(c4))

# class Course:
#     def __init__(self, id, name) -> None:
#         self.id = id
#         self.name = name
#         self.students = []
    
#     def register (self, value):
#         self.name = value
#         self.students.append(value)

#     def is_register(self, value):
#         found = False
#         for s in self.students:
#             if s == value:
#                 found = True
#         return found


# if __name__ == "__main__":
#     c116 = Course('01418116', 'Computer Programming')
#     c114 = Course('01418114', 'Introduction to Computer Science')

#     print(c116.id)
#     print(c114.name)

#     c116.register("Kwan")
#     c114.register("Kwan")
#     c114.register("Ploy")
#     c116.register("Kate")

#     print(c114.is_register("Ploy"))
#     print(c116.is_register("Ploy"))

#     print(c116.students)
#     print(c114.students)


# class Money:
#     def __init__(self, money, currency) -> None:
#         self.money = money
#         self.currency = currency

#     def is_greater(self, other) -> any:
#         if self.currency == other.currency:
#             return self.money > other.money
#         else:
#             return None
        
# if __name__ == '__main__':
#     m1 = Money(100, 'Baht')
#     m2 = Money(150, 'Baht')
#     print(m1.is_greater(m2))
#     print(m2.is_greater(m1))
#     m3 = Money(200, 'Yen')
#     print(m1.is_greater(m3))

# เขียนได้ 2 แบบ ถ้าไม่ติดข้อจำกัดว่าห้าม import Union จะแนะนำอันนี้มากกว่า
# from typing import Union
#     def is_greater(self, other) -> Union[bool, None]:
#         if self.currency == other.currency:
#             return self.money > other.money
#         else:
#             return None

# class Album:
#     def __init__(self, name, singer):
#         self.name = name
#         self.singer = singer
#         self.songs = []

#     def add(self, song):
#         if song not in self.songs:
#             self.songs.append(song)

#     def get_song(self, index):
#         if 0 <= index < len(self.songs):
#             return self.songs[index]

# if __name__ == '__main__':
#     od = Album('Four', 'One Direction')
#     od.add('Steal My Girl')
#     od.add('Night Changes')
#     od.add('Night Changes')
#     od.add('Ready to Run')
#     vs = Album('Album', 'Singer')
#     vs.add('Song1')
#     vs.add('Song2')
#     vs.add('Song3')
#     vs.add('Song3')
#     print(od.get_song(2))
#     print(vs.get_song(1))


# class IceCream:

#     def __init__(self, cone_type, max_scoops) -> None:
#         self.cone_type = cone_type
#         self.max_scoops = max_scoops
#         self.flavors = []

#     def add(self, flavor):
#         if len(self.flavors) < self.max_scoops:
#             self.flavors.append(flavor)

#     def have(self, flavor):
#         return self.flavors.count(flavor)

# if __name__ == '__main__':
#     ic = IceCream('Cone', 3)
#     ic.add('Strawberry')
#     ic.add('Chocolate')
#     ic.add('Strawberry')
#     ic.add('Vanilla')    # ไม่เพิ่มเข้า flavors เนื่องจากเกินจำนวนลูกที่กำหนด
#     print(ic.have('Strawberry'))  # มีรสสตรอเบอร์รี่ 2 ลูก
#     print(ic.have('Vanilla'))     # ไม่มีรสวนิลา


# class Item:
#     def __init__(self,type,detail,amount) -> None:
#         self.type = type
#         self.detail = detail
#         self.amount = amount

#     def __str__(self):
#         return 'Item({0}, {1}, {2})'.format(self.type, self.detail, self.amount)
    
# class Expense:
#     def __init__(self):
#         self.items  = []

#     # เมธอดที่สร้างวัตถุรายรับ
#     def earn(self, detail, amount):
#         item = Item('Earn', detail, amount)
#         self.items.append(item)

#     # เมธอดที่สร้างวัตถุรายจ่าย
#     def pay(self, detail, amount):
#         item =  Item('Pay', detail, amount)
#         self.items.append(item)

#     def total_pay(self)->str:
#         total_pay = 0
#         for item in self.items:
#            if item.type == "Pay":
#                total_pay -= item.amount
#         return str(total_pay)
               
#     def total_earn(self)->str:
#         total_earn = 0
#         for item in self.items:
#            if item.type == "Earn":
#                total_earn += item.amount
#         return str(total_earn)
    
#     def remaining(self)->str:
#         earn = int(self.total_earn())
#         pay = int(self.total_pay())
#         return str(earn + pay)
    
#     def total_for(self, detail)->str:
#         total_for = 0
#         for item in self.items:
#             if detail == item.detail:
#                 if item.type == "Earn":
#                     total_for += item.amount
#                 else:
#                     total_for -= item.amount
#         return str(total_for)
    
#     def list_of(self, detail)->[Item]:
#         list_of = []
#         for item in self.items:
#             if detail == item.detail:
#                 list_of.append(item)
#         return list_of
            
    

# if __name__ == '__main__':
#     expense = Expense()
#     expense.earn('Mom', 500)
#     expense.pay('Book', 100)
#     expense.pay('Van to Kaset', 20)
#     expense.pay('Lunch', 10)
#     expense.pay('Lunch', 20)
#     expense.earn('Sell Ice Cream', 120)
#     print(expense.total_pay())
#     print(expense.total_earn())
#     print(expense.remaining())
#     expense.pay('Mom', 60)
#     print(expense.total_for('Mom'))
#     print(expense.total_for('Lunch'))
#     lst = expense.list_of('Lunch')
#     for item in lst:
#         print(item)