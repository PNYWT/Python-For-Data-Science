from animalsubclass import *

wolfie = Wolf()
leo = Lion()
felix = Cat()
rover = Dog()
minnie = Cat()

animals = []
animals.append(wolfie)
animals.append(leo)
animals.append(felix)
animals.append(rover)

##### first version of polymorphism ผ่าน list #####
print("-------- first version of polymorphism ผ่าน list ------")

for animal in animals:
    animal.make_noise()  # polymorphism

##### second version of polymorphism ผ่าน parameter ใน method #####
print("--------- second version of polymorphism ผ่าน parameter ใน method ------")

def echo(animal):
    animal.make_noise()   # polymorphism
    animal.make_noise()   # polymorphism

echo(leo)
echo(rover)

###### duck typing ###### 
# ไม่ได้เป็น subclass ก็เกิด polymorphism ได้ ถ้ามี method ชื่อเดียวกัน
# เกิดขึ้นกับภาษาโปรแกรมที่ไม่มี type เช่น Python เท่านั้น
# ถ้าทำแบบนี้ในภาษาโปรแกรม C++, Java จะได้ Compile Error
#########################

print("----- duck typing: ไม่ใช่ subclass ก็เกิด polymorphism ได้ ถ้ามี method ชื่อเดียวกัน ----")

class Car:
    def make_noise(self):
        print('brrrrr....')
    
car = Car()
animals.append(car)

for animal in animals:
    animal.make_noise()  # polymorphism
