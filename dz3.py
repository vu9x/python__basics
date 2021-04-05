tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
# Решение для первой части задания: реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
# for a, b in zip(tutors, klasses):
#     answer = a, b
#     print(answer)


def list_gen(list1, list2):
    """Ответ на задание 3"""
    if len(list1) > len(list2):
        list2.append(None)
    for list1_iter, list2_iter in zip(list1, list2):
        yield list1_iter, list2_iter


print(list_gen(tutors, klasses), *list_gen(tutors, klasses))
