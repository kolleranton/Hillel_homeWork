# 1. Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать из исходного файла все слова,
# состоящие не менее чем из семи букв.
#
import re

with open("input_data.txt", "r", encoding="utf-8") as f:
    text = f.read()
    # print(text)
    words = " ".join(re.findall(r"\b\w{7,}\b", text))
    print(words)

if len(words) > 0:
    with open("output_data.txt", "w", encoding="utf-8") as f:
        f.write(words)
else:
    print("No words found!")

#
# 2. Дан текстовый файл. Подсчитать количество слов в нём.