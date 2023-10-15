# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# print(scores.items())
# print(scores.values())
# print(scores.keys())
# score_list = list(scores.values())
# print(score_list)


# w = {50: 150, 150:450, 250: 750, 350: 1050}
# x = {100: 300, 200: 600}
# y = {100: 200, 250: 500, 300: 600, 700: 1400}
# z = {100: 400, 250: 1000}
# x.update(z)
# print(x)
# w.update(z)
# print(w)
# z.update(y)
# print(z)
# y.update(x)
# print(y)

# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# print('Beth'  in scores)
# print(('Zoe', 57) in scores.items())

# floor3_rooms = {'4/4': 1, '4/5': 2, '5/1': 3, '5/2': 4, '5/3': 5}
# classroom_floors = {key:'floor3' for key in floor3_rooms}
# print(classroom_floors)
# class4_year_rooms = {key: 'year4' for key in ['4/4', '4/5']}
# print(class4_year_rooms)
# class5_year_rooms  = {key: 'year5' for key in ['5/1', '5/2', '5/3']}
# print(class5_year_rooms)
# left_wings = {value: key for key, value in floor3_rooms.items() if value in [1, 2, 3]}
# print(left_wings)
# right_wings  = {value: key for key, value in floor3_rooms.items() if value in [4, 5]}
# print(right_wings)

# scores = {'Beth': 66, 'Nancy': 79, 'Pat': 82, 'Zoe': 57, 'Ken': 94}
# scores['Pat'] = 89
# scores2 = scores.copy()
# scores3 = scores
# scores2['Beth'] = 65
# scores['Zoe'] = 63
# print(scores2)
# print(scores3)

# text = input("Enter text: ")
# char_count = {}
# for char in text:
#     if char != ' ':
#         char_count[char] = char_count.get(char, 0) + 1
# print(char_count)
# for char, count in char_count.items():
#     print(f"There are {count} {char}'s")


student_scores = {}
total_below_60 = 0
count_below_60 = 0
while True:
    name = input("Enter name: ")
    if name == 'Q':
        break
    try:
        score = float(input("Enter score: "))
    except ValueError:
        continue
    student_scores[name] = score

print(student_scores)

for name, score in student_scores.items():
    if score < 60:
        total_below_60 += score
        count_below_60 += 1
    print(f"{name} got {score:.2f}")

if count_below_60 > 0:
    average_below_60 = total_below_60 / count_below_60
    print(f"Average scores of students who got below 60 = {average_below_60:.2f}")
else:
    print("No one got below 60.")