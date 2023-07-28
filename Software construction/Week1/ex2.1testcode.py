import math

"""
def find_cylinder_volume(h,r):
    return math.pi*pow(r,2)*h

r = float(input("radius = "))
h = float(input("height = "))
v = find_cylinder_volume(h,r)
print("Volume = %.2f" %v)
"""
# math.cell(2.1) ปัดขึ้น 3
# math.floor(2.9) ปัดลง 2

"""
def poly(x):
    return int(5*pow(x,2)-121*x+7)

x = int(input("AAA ->"))
a = poly(x)
print(a)
"""

# s = (ut) + (1/2 at^2)
"""
def distance(acceleration,time):
    return (1/2) * acceleration * pow(time,2)

acceleration = int(input("Acceleration : "))
time = int(input("Time : "))
print(distance(acceleration,time))
"""


"""
def area_of_circle(k):
    r = k/2  
    return math.pi*pow(r,2)

d = input("Diameter: ")
d_float = float(d)
area = area_of_circle(d_float)
print("area %.3f" %area)
"""


# Please enter the value of L: 5
# Area is 44.6350
"""
def MiniHeart(x):
   areaCircle = math.pi * pow(x/2,2) 
   areaCircle = areaCircle
   areaSquare = x*x
   allArea = areaCircle + areaSquare
   return allArea


value = int(input("Please enter the value of L: "))
area = MiniHeart(value)
print("Area is %.4f" %area)
"""

# ใส่แค่จำนวนวินาทีลงไป
# แล้วแสดงจำนวนชั่วโมง นาทีและวินาทีดังตัวอย่างข้างล่าง
# return ค่าประกอบไปด้วยจำนวนชั่วโมง จำนวนนาที และจำนวนวินาที
# แปลงวินาทีเป็น นาที เป็นชั่วโมง
"""
def caltime(x):
    sec = x % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return hour,min,sec


sInput = int(input("s: "))
h,m,s = caltime(sInput)
print(sInput,"seconds equals",h,"hour(s)",m,"minute(s)","and",s,"second(s)")
"""

# Enter total money: 1218
# 500: 2
# 100: 2
#  20: 0
#   5: 3
#   1: 3

def change(money):
    b = 0.0
    if money >= 500:
        b = money//500
        return b
    elif money >= 100 and money < 500:
        b = money//100
        return b
    elif money >= 20 and money < 100:
        b = money//20
        return b
    elif money >= 5 and money < 10:
        b = money//5
        return b
    elif money >= 1 and money < 5:
        b = money//1
        return b

money = int(input("Enter total money: "))
b500 = change(money)
left = money - b500*500
b100 = change(left)
left = left - b100*100
print("leftleftleftleftleft",left)
#บัคเคสนี้อยู่
b20 = change(left)
left = left - b20*20
b5 = change(left)
left = left - b5*5
b1 = change(left)


print("500: %d" % b500)
print("100: %d" % b100)
print(" 20: %d" % b20)
print("  5: %d" % b5)
print("  1: %d" % b1)