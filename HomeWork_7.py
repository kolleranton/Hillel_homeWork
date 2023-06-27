# Задание 1.
#
# Написать рекурсивную функцию нахождения степени числа.
#
# add_numer = int(input(f"Enter the number: "))
# degree = int(input(f"Enter the degree of the number: "))
#
# def factorial(add_numer, degree):
#     if degree == 1:
#         return add_numer
#     if add_numer != 1:
#         return add_numer * factorial(add_numer, degree - 1)
#
# print(f"The result of exponentiation is: ", factorial(add_numer, degree))

#
#
# Задание 2.
#
# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь.
# Проиллюстрируйте работу функции примером. (протестировать)
#


def number_to_stars(text, n):
    if not n == 0:
        return number_to_stars(text + '*', n - 1)
    else:
        return text

number = int(input("Enter number: "))
result = number_to_stars('', number)

print(result)


#
# Задание 3.
#
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b. Проиллюстрируйте работу функции примером.

# a = int(input(f"Enter the first number: "))
# b = int(input(f"Enter the second number: "))
# def sum_range(a, b):
#
#     if a > b:
#
#         return 0
#
#     return a + sum_range(a+1, b)
#
# print(sum_range(a, b))