# Дан список с названиями фруктов, орехов и ягод.
# Определите, названий начинающихся на какую(какие) букву(буквы) больше всего.
# Известно, что названия могут начинаться как с заглавной, так и с маленькой буквы.
# Примеры
# Дано: ["ананас", "кокос", "Арбуз", "киви", "Клюква", "банан", "хурма"]
# Результат: фруктов на букву "к" больше.
# Дано: ["ананас", "яблоко", "Арбуз", "киви", "Клюква", "банан", "хурма"]
# Результат: фруктов на букву "к"и "а" больше.

info = {
    "stat": []
}
fruits = ["ананас", "кокос", "Арбуз", "киви", "Клюква", "банан", "хурма", "абрикос"]

def find_char(info, char):
    for i, stat in enumerate(info["stat"]):
        if c == stat["char"]:
            return i
    return -1

for fruit in fruits:
    c = fruit[0]
    i = find_char(info, c)
    if i < 0:
        info["stat"].append({"char": c, "count": 1})
    else:
        info["stat"][i]["count"] += 1

fruit_char = []
i = -1
for stat in info["stat"]:
    count = stat["count"]
    if i < 0 or i <= count:
        if i < count:
            fruit_char.clear();
        fruit_char.append(stat["char"])
        i = count

if i >= 0:
    print(f"Результат: фруктов на букву {fruit_char} больше.")
