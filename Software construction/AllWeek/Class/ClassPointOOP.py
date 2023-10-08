class PointOOP:

    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b

    def distance_from_origin(self):
        return ((self.x **2) + (self.y ** 2)) ** 0.5

    
p = PointOOP(3,4)
d = p.distance_from_origin() ## OOP
print(d)