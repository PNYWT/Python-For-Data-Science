# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]
# word = input("Enter a word: ")
# if is_palindrome(word):
#     print(f"{word} is a Palindrome")
# else:
#     print(f"{word} is not a Palindrome")


# def is_valid_ipv4(ip):
#     parts = ip.split(".")
#     if len(parts) != 4:
#         return False
#     for part in parts:
#         try:
#             num = int(part)
#             if num < 0 or num > 255:
#                 return False
#         except ValueError:
#             return False

#     return True

# ip = input("")
# if is_valid_ipv4(ip):
#     print("Valid IP Address")
# else:
#     print("Invalid IP Address")


# def binary_to_decimal(binary):
#     decimal = 0
#     power = 0
#     for digit in reversed(binary):
#         if digit == '1':
#             decimal += 2 ** power
#         power += 1

#     return decimal

# binary = input("Enter binary: ")
# decimal = binary_to_decimal(binary)
# print(decimal)


# text = input("Input text: ")
# n = int(input("N: "))
# lines = [text[i:i+n] for i in range(0, len(text), n)]
# for line in lines:
#     print(line)


# รับข้อความและจำนวนตัวอักษรต่อหลัก
# text = input("Input text: ")
# n = int(input("N: "))
# chunks = [text[i:i + n] for i in range(0, len(text), n)]
# max_len = max(len(chunk) for chunk in chunks)
# formatted_chunks = [chunk.ljust(max_len) for chunk in chunks]
# vertical_text = "\n".join("".join(row) for row in zip(*formatted_chunks))
# print(vertical_text)

# def is_password_strong(password):
#     # Initialize flags for each condition
#     has_length = len(password) >= 8
#     has_upper = any(char.isupper() for char in password)
#     has_lower = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)
#     has_special = any(char in "!@#$%^&*" for char in password)
#     conditions = [has_length, has_upper, has_lower, has_digit, has_special]
#     messages = [
#         "The password length must be greater than or equal to 8",
#         "The password must contain one or more uppercase characters",
#         "The password must contain one or more lowercase characters",
#         "The password must contain one or more numeric values",
#         "The password must contain one or more special characters"
#     ]
#     error_messages = [messages[i] for i in range(5) if not conditions[i]]
#     if not error_messages:
#         return "Your password is strong!"
#     else:
#         return "\n".join(error_messages)
# password = input("Enter a password: ")
# result = is_password_strong(password)
# print(result)



