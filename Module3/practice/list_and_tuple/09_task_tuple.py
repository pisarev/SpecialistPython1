# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.
a = []
b = []
c = []
import random
i = 0
while i < random.randint(10, 100):
    a.append(random.randint(0, 0xffffff))
    i += 1

i = 0
while i < random.randint(10, 100):
    b.append(random.randint(0, 0xffffff))
    i += 1

i = 0
while i < random.randint(10, 100):
    c.append(random.randint(0, 0xffffff))
    i += 1

a = tuple(a)
b = tuple(b)
c = tuple(c)

print(len(a))
print(len(b))
print(len(c))
