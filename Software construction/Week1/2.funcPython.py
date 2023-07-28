def read_Base():
    base = input("Enter Base: ")
    return int(base)

def read_Height():
    height = input("Enter height: ")
    return int(height)

def compute_Area(base,height):
    return 0.5*base*height

def show_Area(area):
    print("Triangle area is",area)

bInput = read_Base()
hInput = read_Height()
calArea = compute_Area(bInput, hInput)
show_Area(calArea)