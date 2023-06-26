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
n = int(input(f"Enter the number: "))
# symbol = "*"
def stars(n):
    if n > 0:
        stars(n-1)
    # return symbol + stars(n - 1)

    # if n >= 1:
    #     return symbol + stars(n-1)

    # print(f"{symbol}")
print("*", end=" ")
    # stars(n - 1)
#

#
# Задание 3.
#
# Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b.
# Пользователь вводит a и b. Проиллюстрируйте работу функции примером.