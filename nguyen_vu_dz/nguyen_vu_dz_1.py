# Домашнее задание 1

# задача номер 1
print("Задача номер 1")

seconds_in_minute = 60
seconds_in_hour = seconds_in_minute * 60
seconds_in_day = seconds_in_hour * 24

user_answer = int(input("введите количество секунд: "))

if user_answer < seconds_in_minute:
    print(user_answer, "сек")
elif user_answer < seconds_in_hour:
    minutes = user_answer / seconds_in_minute
    seconds = user_answer % seconds_in_minute
    print(int(minutes), "min", seconds, "sec")
elif user_answer < seconds_in_day:
    hours = user_answer / seconds_in_hour
    minutes = user_answer % seconds_in_hour / seconds_in_minute
    seconds = user_answer % seconds_in_hour % seconds_in_minute
    print(int(hours), "h", int(minutes), "min", seconds, "sec")
else:
    days = user_answer / seconds_in_day
    hours = user_answer % seconds_in_day / seconds_in_hour
    minutes = user_answer % seconds_in_day % seconds_in_hour / seconds_in_minute
    seconds = user_answer % seconds_in_day % seconds_in_hour % seconds_in_minute
    print(int(days), "d", int(hours), "h", int(minutes), "min", seconds, "sec")


# Задача номер 2
print("Задача номер 2")

# создание листа из куба нечетных числе от 0 до 1000
cube_odd_numbers = []
max_number = 1000
counter = 0

while max_number != counter:
    counter += 1
    if counter % 2 != 0:
        cube_odd_numbers.append(counter ** 3)

print("начальный лист", cube_odd_numbers)

# решение задачи 2.a
answer_a_list = []
answer_a_counter = ''

for a in cube_odd_numbers:
    answer_a_counter = a
    total = 0
    while a > 0:
        digit = a % 10
        total = total + digit
        a = a // 10
    if total % 7 == 0:
        answer_a_list.append(answer_a_counter)

answer_a_total = 0
for a_2 in answer_a_list:
    answer_a_total += a_2

print("Ответ на задание 2.а", answer_a_total)

# решение задачи 2.b
b_list = []
answer_b_list = []
answer_b_counter = ''

for b in cube_odd_numbers:
    b_list.append(b + 17)

for b in b_list:
    answer_b_counter = b
    total = 0
    while b > 0:
        digit = b % 10
        total = total + digit
        b = b // 10
    if total % 7 == 0:
        answer_b_list.append(answer_b_counter)

answer_b_total = 0
for b_2 in answer_b_list:
    answer_b_total += b_2

print("Ответ на задание 2.b", answer_b_total)

# решение задачи 2.c

answer_c_total = 0
for c in cube_odd_numbers:
    answer_c_counter = c + 17
    checker = answer_c_counter

    total = 0
    while checker > 0:
        digit = checker % 10
        total += digit
        checker = checker // 10
    if total % 7 == 0:
        answer_c_total += answer_c_counter

print("Ответ на задание 2.c", answer_c_total)


# задача номер 3
print("Задача номер 3")

user_answer_3 = int(input("Пожалуйста, введите цифру от 1 до 20: "))
percent_name_list = ["процент", "процента", "процентов"]
if user_answer_3 == 1:
    print("Вы ввели", user_answer_3, percent_name_list[0])
elif user_answer_3 < 5:
    print("Вы ввели", user_answer_3, percent_name_list[1])
elif user_answer_3 <= 20:
    print("Вы ввели", user_answer_3, percent_name_list[2])
