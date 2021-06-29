# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #

import math
length = int(input())
matrix = [[" " for j in range(length)] for i in range(length)]

x = 0
y = 0
while x < length:
    y = 0
    while y < length:
        if x == y or length - 1 - x == y:
            matrix[x][y] = "#"
        else:
            matrix[x][y] = " "
        y += 1
    x += 1
for char in matrix:
    print(char)
