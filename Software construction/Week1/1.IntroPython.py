print("hello python")

money = 123.3432
print("total price is %.2f USD" % money)

print(34, 24, 35, 170.0)

print("I'm", 19, "years old")

a,b = 17,35
print(a, b)

print(34, 24, 35, 170.0, sep=',')
print(34, 24, 35, 170.0, sep='')
print("I'm", 19, "years old", sep='-:-')

print("I'm", end=' ')
print(19, end='')
print("yrs.", end='\n')

output = "Hello" + "Python" + "is easy."
print(output)

output = 34 + 24 + 35 + 170.0
print(output)

output = str(34) + str(24) + str(35) + str(170.0)
print(output)

age = 19
output = "I'm " + str(age) + " yrs."
print(output)

# name = input("What is your name?")
# print("Hello,",name+".")
# year = int(input("What is your birth year?"))
# age = 2010 - year
# print("You will be",age,"this year.")

# width = input("width : ")
# length = input("length : ")
# print("area :",float(width)*float(length))
# print("perimeter :",2.0 * (float(width)+float(length)))

"""
summary price : 107
food : 100.0
vat : 7.0
"""

# summary_price = float(input("summary price : "))
# food = (summary_price/107)*100
# print("food :",food)
# print("vat :", summary_price - food)

"""
Energy = Milk * Coffee^2
Milk: 2
Coffee: 3
18
"""
# Milk = int(input("Milk: "))
# Coffee = int(input("Coffee: "))
# print(Milk*pow(Coffee,2))

"""
Money: 10
Son: 2
5 0
"""
# Money = int(input("Money: "))
# Son = int(input("Son: "))
# print(int(Money/Son), Money%Son)


"""
First sentence: CPE
Second sentence: 35
Third sentence: Keep fighting!
70
"""
# First_sentence = input("First sentence: ")
# Second_sentence = input("Second sentence: ")
# Third_sentence = input("Third sentence: ")
# print((len(First_sentence) + len(Second_sentence)) * len(Third_sentence))

"""
Input text: KU
Input number: 81
I can print string with another datatype like this -> KU 125.112
"""
text = input("Input text: ")
number = input("Input number: ")
print("I can print string with another datatype like this ->",text,float(number)+44.112)

