# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

value = int(input())
if value % 3 == 0 and value % 5 == 0:
    print("Foobar")
elif value % 3 == 0:
    print("Foo")
elif value % 5 == 0:
    print("Bar")
