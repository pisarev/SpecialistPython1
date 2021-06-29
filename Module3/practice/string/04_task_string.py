# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

i = 0
j = 0
count = 0
while i < len(text):
    if text[i] == " ":
        if i > 0 and i - j - 1 > 5:
            count += 1
        j = i
    i += 1

print(count)
