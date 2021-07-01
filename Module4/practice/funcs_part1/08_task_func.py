# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci_number(number_index, index = 0, prior_value_1 = 0, prior_value_2 = 0):
    if index == 1:
        prior_value_1 = 1
    if index == number_index:
        return prior_value_1
    return fibonacci_number(number_index, index + 1, prior_value_1 + prior_value_2, prior_value_1)

print(fibonacci_number(int(input())))
