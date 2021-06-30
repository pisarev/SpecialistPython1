# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_length = 0
name_index = -1
for i, name in enumerate(names):
    j = len(name)
    if max_length < j:
        max_length = j        
        name_index = i
if name_index != -1:
    print(names[name_index])
# TODO: your code here
