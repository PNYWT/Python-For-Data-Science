# seq = [8, 20, 'c', 1, 'Hello', 38]
# print(seq[5])

# seq = [2,3,5,7,11,13,17,19]
# for i in range(0,5):
#     print(seq[i])

# for i in range(1,len(seq),3):
#     print(seq[i])

# seq = [10,11,10,9,12,9,8,10]
# seq.sort(reverse=True)
# print(seq)

# nums = [3,10,7,8,6]
# print(min(nums))
# print(max(nums))
# print(sum(nums))


# x = [1,2,3,4,5]
# y = x
# x[3] = 200
# print(x)
# print(y)

"""
Enter a number (just [Enter] to quit): 10↵
Enter a number (just [Enter] to quit): ↵
The maximum is 10.00
The minimum is 10.00
The average is 10.00
"""
# สร้างรายการเพื่อเก็บข้อมูลตัวเลข
# numbers = []

# # รับข้อมูลจากผู้ใช้
# while True:
#     user_input = input("Enter a number (just [Enter] to quit): ")
#     if not user_input:
#         if not numbers:
#             print("Nothing to do.")
#         break
#     try:
#         number = float(user_input)
#         numbers.append(number)
#     except ValueError:
#         print("Please enter a valid number.")

# # ตรวจสอบว่ามีตัวเลขอยู่ในรายการหรือไม่
# if numbers:
#     # คำนวณค่าสูงสุด ค่าต่ำสุด และค่าเฉลี่ย
#     maximum = max(numbers)
#     minimum = min(numbers)
#     average = sum(numbers) / len(numbers)

#     # แสดงผลลัพธ์
#     print(f"The maximum is {maximum:.2f}")
#     print(f"The minimum is {minimum:.2f}")
#     print(f"The average is {average:.2f}")


"""
Enter a number (to exit, just enter 0): 1
Enter a number (to exit, just enter 0): 2.5
Enter a number (to exit, just enter 0): -4
Enter a number (to exit, just enter 0): 3
Enter a number (to exit, just enter 0): -1.8
Enter a number (to exit, just enter 0): 0
The sum of positive numbers is 6.50
The sum of negative numbers is -5.80
"""
# # กำหนดตัวแปรสำหรับเก็บผลรวมของจำนวนบวกและจำนวนลบ
# sum_positive = 0
# sum_negative = 0

# # รับข้อมูลจากผู้ใช้
# while True:
#     user_input = float(input("Enter a number (to exit, just enter 0): "))
    
#     if user_input == 0:
#         break
    
#     if user_input > 0:
#         sum_positive += user_input
#     elif user_input < 0:
#         sum_negative += user_input

# # แสดงผลลัพธ์
# print(f"The sum of positive numbers is {sum_positive:.2f}")
# print(f"The sum of negative numbers is {sum_negative:.2f}")

"""
Enter student score (or just ENTER to end): 10↵
Enter student score (or just ENTER to end): 13↵
Enter student score (or just ENTER to end): 19↵
Enter student score (or just ENTER to end): ↵
Student #1 score: 10
Student #2 score: 13
Student #3 score: 19
Average score is 14.00
Minimum score is 10
Maximum score is 19
"""
# # กำหนดรายการเพื่อเก็บคะแนนของนักเรียน
# scores = []

# # รับคะแนนจากผู้ใช้
# while True:
#     user_input = input("Enter student score (or just ENTER to end): ")
#     if not user_input:
#         break
#     try:
#         score = int(user_input)
#         scores.append(score)
#     except ValueError:
#         print("Please enter a valid score.")

# # ตรวจสอบว่ามีคะแนนอยู่ในรายการหรือไม่
# if not scores:
#     print("No scores entered.")
# else:
#     # คำนวณค่าเฉลี่ย ค่าต่ำสุด และค่าสูงสุด
#     average_score = sum(scores) / len(scores)
#     min_score = min(scores)
#     max_score = max(scores)

#     # แสดงผลลัพธ์
#     for i, score in enumerate(scores, start=1):
#         print(f"Student #{i} score: {score}")
#     print(f"Average score is {average_score:.2f}")
#     print(f"Minimum score is {min_score}")
#     print(f"Maximum score is {max_score}")

"""
Enter student score (or just ENTER to end): 13↵
Enter student score (or just ENTER to end): 19↵
Enter student score (or just ENTER to end): 10↵
Enter student score (or just ENTER to end): ↵
Rank #1: 19
Rank #2: 13
Rank #3: 10
"""
# # กำหนดรายการเพื่อเก็บคะแนนของนักเรียน
# scores = []

# # รับคะแนนจากผู้ใช้
# while True:
#     user_input = input("Enter student score (or just ENTER to end): ")
#     if not user_input:
#         break
#     try:
#         score = int(user_input)
#         scores.append(score)
#     except ValueError:
#         print("Please enter a valid score.")

# # ตรวจสอบว่ามีคะแนนอยู่ในรายการหรือไม่
# if not scores:
#     print("No scores entered.")
# else:
#     # เรียงลำดับคะแนนจากมากไปน้อย
#     ranked_scores = sorted(scores, reverse=True)

#     # แสดงผลลัพธ์
#     for i, score in enumerate(ranked_scores, start=1):
#         print(f"Rank #{i}: {score}")
