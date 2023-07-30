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

# คำนวณหัวใจ
# Please enter the value of L: 5
# Area is 44.6350
"""
def MiniHeart(x):
   areaCircle = math.pi * pow(x/2,2) 
   areaSquare = x*x
   allArea = areaCircle + areaSquare
   return allArea

value = int(input("Please enter the value of L: "))
area = MiniHeart(value)
print("Area is %.4f" %area)
"""

"""
# ใส่แค่จำนวนวินาทีลงไป
# แล้วแสดงจำนวนชั่วโมง นาทีและวินาทีดังตัวอย่างข้างล่าง
# return ค่าประกอบไปด้วยจำนวนชั่วโมง จำนวนนาที และจำนวนวินาที
# แปลงวินาทีเป็น นาที เป็นชั่วโมง
def caltime(x):
#หนึ่งวันมี 24 ชั่วโมง และ 1 ชั่วโมงมี 60 นาที (ครั้งละ 60 วินาที) 
#เราจึงมีทั้งหมด 24 * 60 * 60 = 86,400 วินาที
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

"""
#ทอนเงิน
def change(money,value):
    b = money // value
    return b

# ต้องเติมโค้ดให้สมบูรณ์
money = int(input("Enter total money: "))
b500 = change(money,500)
left = money - b500*500
b100 = change(left,100)
left = left - b100*100
b20 = change(left,20)
left = left - b20*20

b5 = change(left,5)
left = left - b5*5
b1 = change(left,1)

print("500: %d" % b500)
print("100: %d" % b100)
print(" 20: %d" % b20)
print("  5: %d" % b5)
print("  1: %d" % b1)
"""

"""
#หลักเลข
def digit(num):
   if num >= 0 and num <= 9999:
      return num % 10
   
def tens(num):
   if num >= 0 and num <= 9999:
      return (num // 10) % 10
   
def hundreds(num):
   if num >= 0 and num <= 9999:
      return (num // 100) % 10
   
def thousands(num):
   if num >= 0 and num <= 9999:
      return num // 1000
   

def sum_digits(num):
    if num >= 0 and num <= 9999:
        allNumber = (digit(num), tens(num), hundreds(num), thousands(num))
        sumNumber = sum(allNumber)
        return sumNumber

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))
"""


"""
# เดินเรือ
#(not necessary) declare global variable that will be use in subroutine
price_a=0
price_b=0
price_c=0
price_s=0
price_o=0
weight_a=0
weight_b=0
weight_c=0
weight_o=0
distance_oa=0
distance_ab=0
distance_bc=0
distance_co=0

def travel_speed(w):
    #calculate traveling speed using a formular that is given in the problem
    return 90/(30+w)+5

from math import ceil

def travel_time(s, d):
    #calculate total days to travel distance d using speed s.
       A fraction of day is roundup to full day
    hours = d/s
    day = ceil(hours/24)
    return day

def cal_sub_profit(distance, net_weight, sell_weight, cargo_price_per_ton, supply_price_per_day):
    #calculate profit that is received when travel from a town to a next town
    speed = travel_speed(net_weight)
    cargo_price = sell_weight*cargo_price_per_ton
    supply_price = travel_time(speed,distance)*supply_price_per_day
    return cargo_price - supply_price

def calculate_profit():
    #calculate and return result profit from input data
    #step 1: from o to a
    w_net = weight_a+weight_b+weight_c
    profit = cal_sub_profit(distance_oa,w_net,weight_a,price_a,price_s)
    #step 2: from a to b
    w_net = weight_b+weight_c
    profit = profit + cal_sub_profit(distance_ab,w_net,weight_b,price_b,price_s)
    #step 3: from b to c
    w_net = weight_c
    profit = profit + cal_sub_profit(distance_bc,w_net,weight_c,price_c,price_s)
    #step 4: from c to O
    w_net = weight_a+weight_b+weight_c
    profit = profit + cal_sub_profit(distance_co,w_net,weight_o,price_o,price_s)
    return profit

def read_input():
    #read input and store in global variable
    # need to declare variables as global variables because we need to assign their values
    global price_a, price_b, price_c, price_s, price_o
    global weight_a, weight_b, weight_c,weight_o
    global distance_oa, distance_ab, distance_bc, distance_co
    weight_a = float(input("weight of cargo to A: "))
    weight_b = float(input("weight of cargo to B: "))
    weight_c = float(input("weight of cargo to C: "))
    weight_o = float(input("weight of cargo to O: "))
    price_a = float(input("price of cargo to A: "))
    price_b = float(input("price of cargo to B: "))
    price_c = float(input("price of cargo to C: "))
    price_o = float(input("price of cargo to O: "))
    price_s = float(input("price of supply: "))
    distance_oa = float(input("distance O to A: "))
    distance_ab = float(input("distance A to B: "))
    distance_bc = float(input("distance B to C: "))
    distance_co = float(input("distance C to O: "))

# main program

# weight of cargo to A: 1
# weight of cargo to B: 2
# weight of cargo to C: 3
# weight of cargo to O: 6
# price of cargo to A: 30
# price of cargo to B: 20
# price of cargo to C: 10
# price of cargo to O: 30
# price of supply: 10
# distance O to A: 100
# distance A to B: 100
# distance B to C: 200
# distance C to O: 50
# result profit is 230.000
read_input()
profit = calculate_profit()
print("result profit is %.3f"%profit)
"""

#ดอกเบี้ย
"""
# Enter principle: 25000
# Enter interest rate: 3.25
# Enter time: 6.5
# Return money for simple interest calculation is 30281.25 Baht.
# Return money for compound interest calculation is 30776.94 Baht.

def simple_interest(p, r, t):
    #principal + (principal * interest_rate * time)
    return p + (p * r/100 * t)

def compound_interest(p, r, t):
    #เงินต้น x (1 +อัตราดอกเบี้ย)^ระยะเวลากู้ยืม
    return p * (1+r/100)**t


p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))
"""

#ระยะเวลา
"""
Start time:
>> Enter hour: 8
>> Enter minute: 15
>> Enter second: 0
Finish time:
>> Enter hour: 13
>> Enter minute: 20
>> Enter second: 0
Elapsed time is 5 hours 5 minutes 0 seconds.
"""
def read_hour():
    while True:
        try:
            hour = int(input("Enter hour: "))
            if 0 <= hour <= 23:
                return hour
            else:
                print("Invalid input. Please enter an hour in the range 0-23.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def read_minute():
    while True:
        try:
            minute = int(input("Enter minute: "))
            if 0 <= minute <= 59:
                return minute
            else:
                print("Invalid input. Please enter a minute in the range 0-59.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def read_second():
    while True:
        try:
            second = int(input("Enter second: "))
            if 0 <= second <= 59:
                return second
            else:
                print("Invalid input. Please enter a second in the range 0-59.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# change to second
def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

# Convert start - finish to hours, minutes, and seconds
def time_elapsed(start, finish):
    elapsed_seconds = finish - start 
    hours = elapsed_seconds // 3600
    minutes = (elapsed_seconds% 3600) // 60
    seconds = elapsed_seconds % 60
    return "{} hours {} minutes {} seconds.".format(hours, minutes, seconds)

# read time and change to second
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

# Read start time
print('Start time:')
start_time = read_time()

# Read finish time
print('Finish time:')
finish_time = read_time()

print('Elapsed time is', time_elapsed(start_time, finish_time))
