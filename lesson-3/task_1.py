"""
1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и
    выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
    обработку ситуации деления на ноль.
"""


def div(value1, value2):
    """
    Функция деления двух чисел
    :param value1: Делимое
    :param value2: Делитель
    :return:
    """

    try:
        result = float(value1) / float(value2)
    except ZeroDivisionError:
        result = "Error. Division by zero."
    except ValueError:
        result = "Value Error"

    return result


USR_VALUE = input(
    f"Введите операцию деления двух чисел через знак '/'(Например: 4/2):").split('/')
if len(USR_VALUE) == 2:
    print(div(USR_VALUE[0], USR_VALUE[1]))
else:
    print("There is no div operation")
