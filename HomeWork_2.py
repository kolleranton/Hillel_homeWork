# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран максимум
# из трёх, минимум из трёх или среднеарифметическое трёх чисел.

num_1 = int(input("Input  num 1:"))
num_2 = int(input("Input num 2:"))
num_3 = int(input("Input num 3:"))
num_list = [num_1, num_2, num_3]

user_select = int(input("Enter 1 to get max, Enter 2 to get min, Enter 3 to get average:"))

if user_select == 1:
    print("Max:", max(num_list))
elif user_select == 2:
    print("Min:", min(num_list))
elif user_select == 3:
    print("Average:", sum(num_list) / len(num_list))
else:
    print("Wrong choice, use 1 or 2 or 3")


# 2. Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит
# метры в мили, дюймы или ярды.


numer = int(input("Enter number in meters:"))

user_select = int(input("Enter 1 if you want to earn miles:\nEnter 2 if you want to get inches:\nEnter 3 if you want to get yards:\n"))

if user_select == 1:
    print("Miles:", (numer * 0.000621371192))
elif user_select == 2:
    print("Inches:", (numer * 39.370078740157))
elif user_select == 3:
    print("Yards:", (numer * 1.09))
else:
    print("incorrect choice:")

