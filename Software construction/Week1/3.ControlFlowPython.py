# def num_candies(want, limit):
#     if want < limit:
#         return limit
#     return want

# limit = 7
# x = int(input("How many?: "))
# print("You should buy",num_candies(x,limit),"candies.")

# n = int(input("input number: "))
# if n%2 == 0:
#     print("even number")
# else:
#     print("odd number")

# a = int(input())
# b = int(input())

# if a%b == 0:
#    print("YES")
# else:
#    print("NO")

"""
ถ้า n เป็นเลขคี่ ให้พิมพ์ "Weird"
ถ้า n เป็นเลขคู่ และอยู่ในช่วงตั้งแต่ 2 ถึง 5 รวมถึงตัวเลขดังกล่าว ให้พิมพ์ "Not Weird"
ถ้า n เป็นเลขคู่ และอยู่ในช่วงตั้งแต่ 6 ถึง 20 รวมถึงตัวเลขดังกล่าว ให้พิมพ์ "Weird"
ถ้า n เป็นเลขคู่ และมากกว่า 20 ให้พิมพ์ "Not Weird"
Enter a number (1-100): 1
Weird
Enter a number (1-100): 4
Not Weird
Enter a number (1-100): 18
Weird
Enter a number (1-100): 98
Not Weird
"""
# n = int(input("Enter a number (1-100): "))

# if n%2 != 0: #เลขคี่
#     print("Weird")
# elif n%2 == 0 and n >= 2 and n <= 5:
#     print("Not Weird")
# elif n%2 == 0 and n >= 6 and n <= 20:
#     print("Weird")
# elif n%2 == 0 and n > 20:
#     print("Not Weird")

#จงเขียนโปรแกรมรับค่าจำนวนจริง (ที่มีทั้งจำนวนเต็มและทศนิยม) 2 ค่า คือ x และ y 
# แล้วพิมพ์ว่าจุดนี้อยู่ในจตุภาค (Quadrant) หรือ แกนใด (Axis) หรือ จุด origin
"""
Enter x: 1.01
Enter y: 1
1
Enter x: -1
Enter y: 1
2
Enter x: -1 
Enter y: -1
3
Enter x: 1
Enter y: -1
4
Enter x: 1
Enter y: 0
x-axis
Enter x: 0
Enter y: 1
y-axis
Enter x: 0 
Enter y: 0
Origin
"""
# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# if x > 0 and y == 0:
#     print("x-axis")
# elif x == 0 and y > 0:
#     print("y-axis")
# elif x == 0 and y == 0:
#     print("Origin")
# elif x > 0 and y > 0:
#     print("1")
# elif x < 0 and y > 0:
#     print("2")
# elif x < 0 and y < 0:
#     print("3")
# elif x > 0 and y < 0:
#     print("4")


"""
อัตราค่าบริการชั่วโมงละ 900 บาท ----
เศษชั่วโมงที่มากกว่า 20 นาทีจะปัดเป็น 1 ชั่วโมง (เช่น 1ชั่วโมง 30 นาที คิดเป็น 2 ชั่วโมง) ----
หากใช้บริการตั้งแต่ 2 ชั่วโมงขึ้นไป แต่ไม่ถึง 4 ชั่วโมง จะลดราคา 10%
หากใช้บริการ 4 ชั่วโมง จะลดราคา 20%
หากใช้บริการตั้งแต่ 5 ชั่วโมงขึ้นไป จะลดราคา 30%
จงเขียนโปรแกรมเพื่อคำนวณอัตราค่าบริการเป็นจำนวนเต็ม โดยรับค่าเวลาเป็นหน่วยนาที (กำหนดให้เวลาเป็นจำนวนเต็มบวกเสมอ)

How long have Buzz played ?: 390
Total price is 4410 baht.
How long have Buzz played ?: 195
Total price is 2430 baht.
"""

# minTime = int(input("How long have Buzz played ?: "))
# payHour = 900
# minToHour = minTime//60
# totalPay = minToHour * payHour

# if minTime - minToHour * 60 > 20:
#     minTime = minTime - minTime%60 + 60
#     minToHour = minTime//60
#     totalPay = minToHour * payHour

# if minToHour >= 2 and minToHour < 4:
#     totalPay -= totalPay*0.10
# elif minToHour >= 4 and minToHour < 5:
#     totalPay -= totalPay*0.20
# elif minToHour >= 5:
#     totalPay -= totalPay*0.30

# print("Total price is %.0f" %totalPay,"baht.")

"""
Child (0-12 years)
Adolescence (13-18 years)
Adult (19-59 years)
Senior Adult (60 years and above)

Enter your age : 11
You are Child.

Enter your age : 18
You are Adolescence.

Enter your age : 65
You are Senior Adult.
"""

# age_Input = int(input("Enter your age : "))

# if age_Input >= 0 and age_Input <= 12:
#     print("You are Child.")
# elif age_Input >= 13 and age_Input <= 18:
#     print("You are Adolescence.")
# elif age_Input >= 19 and age_Input <= 59:
#     print("You are Adult.")
# elif age_Input >= 60:
#     print("You are Senior Adult.")


"""
เครื่องคิดเลขอย่างง่าย

รับตัวเลข 2 จำนวน x และ y เป็นจำนวนเต็ม
เครื่องหมายคำนวณซึ่งมีให้เลือก5 ชนิด คือ + - * / % 
หากใส่เครื่องหมายไม่ตรงกับ 5 ชนิดนี้ ให้แสดงว่า Unknown Operator
โดยทศนิยมให้แสดงเพียง2ตำแหน่งเมื่อเป็นการหาร
"""
# x = int(input("x: "))
# operator = input("Operator: ")
# y = int(input("y: "))

# if operator == "+":
#     print(x+y)
# elif operator == "-":
#     print(x-y)
# elif operator == "*":
#     print(x*y)
# elif operator == "/":
#     answ = x/y
#     print("%.2f" %answ)
# elif operator == "%":
#     print(x%y)
# else:
#     print("Unknown Operator")

# BMI
# weight = int(input("Weight: "))
# height = int(input("Height: "))
# BMI = weight/(height/100)**2

# if BMI >= 30:
#     print("Your BMI is %.1f You're in the obese range." %BMI)
# elif BMI < 30 and BMI >= 25:
#     print("Your BMI is %.1f You're in the overweight range." %BMI)
# elif BMI < 25 and BMI >= 18.6:
#     print("Your BMI is %.1f You're in the healthy weight range." %BMI)
# elif BMI < 18.6:
#     print("Your BMI is %.1f You're in the underweight range." %BMI)


"""
บริษัท ACME จำกัด ต้องการให้ส่วนลดกับลูกค้าที่ซื้อสินค้าในมูลค่าตั้งแต่ 1,000 บาทขึ้นไป 
โดยถ้าลูกค้าซื้อสินค้าตั้งแต่ 1,000 ขึ้นไปแต่น้อยกว่า 3,000 บาท ให้ส่วนลด 10% 
และถ้าซื้อสินค้าตั้งแต่ 3,000 บาทขึ้นไป ให้ส่วนลด 15% 
จงเขียนโปรแกรมที่รับจำนวนราคาสินค้าแล้วคำนวนเงินสุทธิที่ลูกค้าต้องชำระ

Enter buying amount: 4200.0
Amount due after discount is 3570.00 baht.
"""

# customer_Pay = float(input("Enter buying amount: "))

# if customer_Pay >= 1000 and customer_Pay < 3000:
#     customer_Pay -= customer_Pay * 10/100
# elif customer_Pay >= 3000:
#     customer_Pay -= customer_Pay * 15/100

# print("Amount due after discount is %.2f baht." %customer_Pay)

"""
Write a program to check username and password for accessing computer system with admin account.

The admin account is "Username=admin" and "Password=Ad31n15Tr@t012".

Use constant variable ADMIN_USERNAME and ADMIN_PASSWORD when you check username and password
"""
# ADMIN_USERNAME = 'admin'
# ADMIN_PASSWORD = 'Ad31n15Tr@t012'

# username = input("Username: ")
# password = input("Password: ")

# if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
#     print("Welcome, admin.")
# elif username == ADMIN_USERNAME and password != ADMIN_PASSWORD:
#     print("You are not admin.")
# else:
#     print("You are not admin.")

# bulotelli Will Bulotelli play?

# injured = input("Is Bulotelli injured?(y/n) ")

# if injured.lower() == "y":
#     print("Not available")
# else:
#     lateTraining = input("Is Bulotelli late for the training?(y/n) ")
#     if lateTraining.lower() == "n":
#         print("Starter")
#     else:
#         performTraining = input("Did Bulotelli perform well in training?(y/n) ")
#         if performTraining.lower() == "y":
#             print("Substitute")
#         else:
#             print("Not selected")


TVs = int(input("How many TVs? "))
dvdPlayers = int(input("How many DVD players? "))
audioSys = int(input("How many Audio Systems? "))

product = {"TV":6000,
           "DVD player":1500,
           "Audio Systems":3000}

totalPay = 0

if TVs >= 1:
    totalPay += product["TV"]*TVs
elif dvdPlayers >= 1:
    totalPay += product["DVD player"]*dvdPlayers
elif audioSys >= 1:
    totalPay += product["Audio Systems"]*audioSys

print("Total price is %.2f baht." %totalPay)