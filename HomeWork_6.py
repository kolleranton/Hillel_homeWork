# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.

# num_1 = int(input("Input  num 1:"))
# num_2 = int(input("Input num 2:"))
# num_3 = int(input("Input num 3:"))
# num_4 = int(input("Input  num 4:"))
# num_5 = int(input("Input num 5:"))
# num_6 = int(input("Input num 6:"))
#
# list_num = [num_1, num_2, num_3, num_4, num_5, num_6]
# def list_elements(list_num):
#     sum_1 = 1
#     for i in list_num:
#         if i > 0:
#             sum_1 *= i
#     return sum_1
#
# print(list_elements(list_num))

#
# Задание 2
# Напишите функцию для нахождения минимума в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.


# num_1 = int(input("Input  num 1:"))
# num_2 = int(input("Input num 2:"))
# num_3 = int(input("Input num 3:"))
# num_4 = int(input("Input  num 4:"))
# num_5 = int(input("Input num 5:"))
# num_6 = int(input("Input num 6:"))
#
# list_num = [num_1, num_2, num_3, num_4, num_5, num_6]
# def min_num(list_num):
#     min(list_num)
#     return min(list_num)
#
# print("Minimum value:  ", min(list_num))

# Задание 3
# Напишите функцию, определяющую количество простых чисел в списке целых.
# Список передаётся в качестве параметра. Полученный результат возвращается из функции.
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def is_simple(number: int) -> bool:
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#         return True
#
#     return False
#
# def show_simple_numbers(numbers) -> None:
#     for number in numbers:
#         if is_simple(number):
#             print(number)
#
#
# show_simple_numbers(numbers=nums)

# это решение скачал с вашего файла. не было времени подумать. разобрал как пример.
#
#
# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное число.
# Из функции нужно вернуть количество удаленных элементов.

list_num = [11, 56, 23, 47, 345, 45, 56]

dell_num = int(input(f"Enter the number you want to delete:  "))

num_1 = 0


def final_list(dell_num):
    for i in list_num:
        if i == dell_num:
            list_num.remove(dell_num)
        return dell_num

print(final_list(dell_num))

#
#
# Задание 5
# Напишите функцию, которая получает два списка в качестве параметра и возвращает список,
# содержащий элементы обоих списков.

# list_1 = [15, 25, 45, 56, 67]
# list_2 = [87, 43, 88, 345, 7]
# list_unit = []
#
#
# def list_double(list_unite):
#     for i in list_1:
#         list_unite.append(i)
#     for i in list_2:
#         list_unite.append(i)
#     return list_unite
#
#
# print(list_double(list_unit))

#
# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента списка целых.
# Значение для степени передаётся в качестве параметра, список тоже передаётся в качестве параметра.
# Функция возвращает новый список, содержащий полученные результаты.
