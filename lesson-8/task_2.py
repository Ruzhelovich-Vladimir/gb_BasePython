"""
2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления
    на нуль. Проверьте его работу на данных, вводимых пользователем.
    При вводе пользователем нуля в качестве делителя программа должна
    корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(ZeroDivisionError):
    """Класс исключения деления на ноль"""

    def __str__(self):
        return "infinity"


try:
    VAL1 = float(input('Введите делимое: '))
    VAL2 = float(input('Введите делитель: '))
    if VAL2 == 0:
        raise MyZeroDivisionError()
except ValueError as err:
    print(f"Ошибочное значение {err.args}")
except MyZeroDivisionError as err:
    print(f"Частное: {err}")
else:
    print(f"Частное: {VAL1 / VAL2}")
