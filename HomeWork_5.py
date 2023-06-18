# В списке целых, заполненном случайными числами вычислить:
# Сумму отрицательных чисел;
# Сумму четных чисел;
# Сумму нечетных чисел;
# Произведение элементов с индексами кратными 3;
# Произведение элементов между минимальным и максимальным элементом;
# Сумму элементов, находящихся между первым и последним положительными элементами.

# import random
#
# num_size = 10
# sum_1 = 0
# sum_2 = 0
# sum_3 = 0
# sum_4 = 1
#
# numer = []
#
# for i in range(num_size):
#     numer.append(random.randint(-10, 10))
# print(f"List of random numbers: {numer}")
#
#
# for i in numer:
#     if i < 0:
#         sum_1 += i
#     elif i % 2 == 0:
#         sum_2 += i
#     elif i % 2 == 1:
#         sum_3 += i
# print(f"Sum of negative numbers: {sum_1}")
# print(f"Sum of even numbers: {sum_2}")
# print(f"The sum of odd numbers: {sum_3}")
#
# result = numer[::3]
# for i in numer:
#     if i == result:
#         sum_4 *= i
# print(f"Product of elements with index 3: {sum_4}")



import random

num_size = 10

numer = []

for i in range(num_size):
    numer.append(random.randint(1, 100))
print(f"List of random numbers: {numer}")

min_value = min(numer)
max_value = max(numer)

sum_5 =
len_list = []

print(min_value)
print(max_value)

min_index = numer.index(min_value)
max_index = numer.index(max_value)
print(min_index)
print(max_index)


for i in range(min_index, max_index):




# Есть список целых, заполненный случайными числами. На основании данных этого массива нужно:

# ■ Создать список целых, содержащий только четные числа из первого списка;
#
# ■ Создать список целых, содержащий только нечетные числа из первого списка;
#
# ■ Создать список целых, содержащий только отрицательные числа из первого списка;
#
# ■ Создать список целых, содержащий только положительные числа из первого списка.
#
# import random
#
# num_size = 10
#
# numer = []
#
# even_numbers = []
# odd_numbers = []
# negative_numbers = []
# positive_numbers = []
#
#
# for i in range(num_size):
#     numer.append(random.randint(-100, 100))
# print(f"List of random numbers: {numer}")
#
# for i in numer:
#     if i % 2 == 0 and i > 0:
#         even_numbers.append(i)
# print("Even numbers: ", even_numbers)
#
# for i in numer:
#     if i % 2 == 1 and i > 0:
#         odd_numbers.append(i)
# print("Odd numbers: ", odd_numbers)
#
# for i in numer:
#     if i < 0:
#         negative_numbers.append(i)
# print("Negative numbers: ", negative_numbers)
#
# for i in numer:
#     if i > 0:
#         positive_numbers.append(i)
# print("Positive_numbers: ", positive_numbers)
