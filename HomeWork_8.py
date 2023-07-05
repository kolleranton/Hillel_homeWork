# Написать валидации с помощью регулярных выражений:
# мобильный номер телефона (только цифры, возможное наличие плюса, длина номера)
#
import re

telefon_nummer = ["+380958585885"]

for val in telefon_nummer:
    if re.match(r"[+]{0,1}[380][0-9]{7}", val) and len(val) == 13:
        print('yes')
    else:
        print('no')

# - домашний номер телефона (только цифры и длина номера)
#
home_nummer = ["2544596"]

for val in home_nummer:
    if re.match(r"\d{5,10}", val) and len(val) == 7:
        print('yes')
    else:
        print('no')



# - email (наличие @, домена: gmail.com например, минимальная длина и максимальная на ваш выбор)
#
email = ["kolleranton@gmail.com"]

for val in email:
    if re.match(r"[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][gmail]+[.][com]{2,}", val):
        print('yes')
    else:
        print('no')



# - ФИО клиента (3 слова, минимальная длина 2 символа, максимальная длина 20)

home_nummer = ["Сергеев Сергей Сергеевич"]

for val in home_nummer:
    if re.match(r"[A-Za-zА-Яа-я]{2,20}\s[A-Za-zА-Яа-я]{2,20}\s[A-Za-zА-Яа-я]{2,20}", val):
        print('yes')
    else:
        print('no')