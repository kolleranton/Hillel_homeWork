# 1. Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.

# try:
#     user_select = int(input("Enter the number of the day of the week here:"))
#
#     if user_select == 1:
#         print("Monday")
#     elif user_select == 2:
#         print("Tuesday")
#     elif user_select == 3:
#         print("Wednesday")
#     elif user_select == 4:
#         print("Thursday")
#     elif user_select == 5:
#         print("Friday")
#     elif user_select == 6:
#         print("Saturday")
#     elif user_select == 7:
#         print("Sunday")
#     else:
#         print("Incorrect numer")
#
# except Exception as error:
#     print(f"Exception occurred: {error}")





# 2. Пользователь вводит два числа. Определить, равны ли эти числа и если нет, вывести их на экран в порядке возрастания

# try:
#     num1 = int(input("Enter the first numer:"))
#     num2 = int(input("Enter the second numer:"))
#
#     if num1 == num2:
#         print("These numbers are equal")
#     elif num1 > num2:
#         print(num2,num1)
#     elif num2 > num1:
#         print(num1,num2)
#
# except Exception as error:
#     print(f"Exception occurred: {error}")





# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат

try:
    num1 = int(input("Enter the first numer:"))
    num2 = int(input("Enter the second numer:"))

    user_select = int(input("Enter 1 if you want to <*>\nEnter 2 if you want to </>\nEnter 3 if you want to <->\nEnter 4 if you want to <+>:"))


    if user_select == 1:
        print(num1 * num2)
    elif user_select == 2:
        print(num1 / num2)
    elif user_select == 3:
        print(num1 - num2)
    elif user_select == 4:
        print(num1 + num2)
    else:
        print("Incorrect numer:")


except ZeroDivisionError as error:
    print(f"ZeroDivisionError occurred: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")