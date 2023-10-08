class Point:

    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other: object) -> bool:
        return not self == other
    
    ##accessor method
    def distance_from_origin(self):
        return ((self.x **2) + (self.y ** 2)) ** 0.5
    
    ##accessor method
    def distance_from(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
    
    ##mutator method
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
    def __str__(self) -> str:
        return "{0}, {1}".format(self.x,self.y)
    
if (__name__ == "__main__"):
    p1 = Point(3,4)
    p2 = Point(3,4)
    p3 = p1

    print("p1.x ->",p1.x)
    print("p2.x ->",p1.y)

    print("p1 is p2:", str(p1 is p2))
    print("p1 is p3:", str(p1 is p3))

    print("p1 == p2:", str(p1 == p2))
    print("p1 != p2:", str(p1 != p2))

    print(p1)
