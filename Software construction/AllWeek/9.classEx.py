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

