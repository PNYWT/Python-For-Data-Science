from point import Point

# Rectangle Has-A (corner) Point  ไม่ใช่ inheritance

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

    def __str__(self):
        return "corner = {0}, width = {1}, height = {2}".format(str(self.corner), self.width, self.height) 


if (__name__ == '__main__'):
    p1 = Point(1,1)
    r1 = Rectangle(p1, 4, 5)
    print('area =', r1.area())

