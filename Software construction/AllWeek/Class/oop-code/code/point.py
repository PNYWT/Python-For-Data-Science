class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other

    ## ---- accessor method ---- ##
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    ## ---- accessor method ---- ##
    def distance_from(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    ## ---- mutator method ---- ##
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

if (__name__ == '__main__'):
    p1 = Point(3,4)  
    print(p1)

    ## 3 ตัวแปร คือ p1, p2, p3 แต่มีแค่ 2 object
    p2 = Point(3,4)
    
    ## p1 และ p3 ชี้มาที่ก้อน object ก้อนเดียวกัน
    p3 = p1

    print("p1 is p2: ",   str(p1 is p2) )
    print("p1 is p3: ",   str(p1 is p3) )

    print("p1 == p2: ",   str(p1 == p2) )
    print("p1 != p2: ",   str(p1 != p2) )

