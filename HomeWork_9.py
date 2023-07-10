# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из исходного файла все слова,
# состоящие не менее чем из семи букв.
#
# import re
#
# with open("input_data.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     # print(text)
#     words = " ".join(re.findall(r"\b\w{7,}\b", text))
#     print(words)
#
# if len(words) > 0:
#     with open("output_data.txt", "w", encoding="utf-8") as f:
#         f.write(words)
# else:
#     print("No words found!")

#
# 2. Дан текстовый файл. Подсчитать количество слов в нём.



with open("my.txt", "w") as test_file:
    test_file.write("To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer"
                    " The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,"
                    " And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache"
                    " and the thousand natural shocks That flesh is heir to, 'tis a consummation Devoutly to be wish'd."
                    " To die, to sleep")
file = open("my.txt")
words = 0

for line in file:
    words += len(line.split())
print("Number of words in this text:", words)