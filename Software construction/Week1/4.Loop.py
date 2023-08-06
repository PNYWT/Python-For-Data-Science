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
Enter a string: xy
Enter arrow's size (greater than 0): 9
xy
 xy
  xy
   xy
    xy
   xy
  xy
 xy
xy
"""

# def print_arrow(string, size):
#     if size <= 0:
#         print("Size must be greater than 0.")
#     else:
#         for i in range(size):
#             print(" " * i + string)
#         for i in range(size - 1, 0, -1):
#             print(" " * i + string)

# input_string = input("Enter a string: ")
# arrow_size = int(input("Enter arrow's size (greater than 0): "))

# print_arrow(input_string, arrow_size)

import math
arr = []
def addValueArr():
    a = int(input("Input a: "))
    arr.append(a)
    b = int(input("Input b: "))
    arr.append(b)
    c = int(input("Input c: "))
    arr.append(c)
    d = int(input("Input d: "))
    arr.append(d)
    e = int(input("Input e: "))
    arr.append(e)

def calMeanAndSD(arrTmp):
    mean = sum(arrTmp)/len(arrTmp)
    print("mean: %.3f" %mean)
    sd = math.sqrt(sum((x - mean) ** 2 for x in arrTmp) / len(arrTmp))
    print("sd: %.3f" %sd)


addValueArr()
calMeanAndSD(arr)