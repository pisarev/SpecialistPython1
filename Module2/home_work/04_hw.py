# Дан размер стороны квадрата. Вывести его стороны символами #.
# Формат входных данных
# На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных
# Требуется вывести диагонали символами # (см. пример)

# Пример:
# Входные данные
# 6
# Выходные данные
######
#    #
#    #
#    #
#    #
######

import math
length = int(input())
matrix = [["" for j in range(length)] for i in range(length)]

x = 0
y = 0
while x < length:
    y = 0
    while y < length:
        if x == 0 or x == length - 1 or y == 0 or y == length - 1:
            matrix[x][y] = "#"
        else:
            matrix[x][y] = " "
        y += 1
    x += 1
for char in matrix:
    print(char)
