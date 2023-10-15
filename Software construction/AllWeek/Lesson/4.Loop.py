"""
Input number: 4
1 
1 2 
1 2 3 
1 2 3 4
"""
# num = int(input("Input number: "))

# def print_number_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
# print_number_pattern(num)

"""
Input number: 7
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxx
xxxxx
xxxx
xxx
xx
x
"""

# def callInput():
#     num = int(input("Input number: "))
#     if num % 2 == 0:
#         print("Please input odd number")
#         callInput()
#     else:
#         print_x_pattern(num)

# def print_x_pattern(n):
#     for i in range(1, n + 1):
#         print("x" * i)

#     for i in range(n - 1, 0, -1):
#         print("x" * i)

# callInput()

"""
How many day : 5
Input price in day 1 : 123.5
Input price in day 2 : 120.65
Input price in day 3 : 210.1
Input price in day 4 : 45
Input price in day 5 : 52
Summary price = 514.85
"""

# day = int(input("How many day : "))
# discount = 5/100
# arrPerDayPrice = []
# totalPrice = 0
# for i in range(day):
#     perDayPrice = float(input(f"Input price in day {i+1} : "))
#     arrPerDayPrice.append(perDayPrice)
#     if len(arrPerDayPrice) >= 2:
#         discount += 1/100
#         totalPrice += arrPerDayPrice[i] - (arrPerDayPrice[i]*discount)
#     else:
#         totalPrice += arrPerDayPrice[i] - (arrPerDayPrice[i]*discount)

# print("Summary price = %.2f" %totalPrice)

"""
Enter your guess (0 - 100): 45
Sorry, your guess is too low, try again later.
Enter your guess (0 - 100): 99
Sorry, your guess is too high, try again later.
Enter your guess (0 - 100): -5
Sorry, out of range, try again later.
Enter your guess (0 - 100): 72
Congratulations, your guess is correct.
"""

# target = 72
# guess = None

# while guess != target:
#     guess = int(input("Enter your guess (0 - 100): "))
#     if guess < 0 or guess > 100:
#         print("Sorry, out of range, try again later.")
#     elif guess < target:
#         print("Sorry, your guess is too low, try again later.")
#     elif guess > target:
#         print("Sorry, your guess is too high, try again later.")
#     else:
#         print("Congratulations, your guess is correct.")
#         break


"""
Enter a string: *
Enter arrow's size (greater than 0): 3
*
 *
*
"""
rows = int(input("Enter arrow's size (greater than 0): "))

for row in range(0,rows):
    for col in range(0,rows):
        if (row-col==3) or (col-row==3):
            print("*",end="")
        else:
            print("",end="")