"""
5)	Создать (программно) текстовый файл, записать в него программно набор
    чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел
    в файле и выводить ее на экран.
"""

from random import random

FILENAME = "task_5.txt"

try:
    USR_NUM_COUNT = int(input("Введите какое кол-во чисел необходимо записать в файл:"))
    SUM1 = 0
    with open(file=FILENAME, mode="w", encoding="utf-8") as f:
        for _ in range(USR_NUM_COUNT):
            VAL = round(random() * 1000, 3)
            SUM1 += VAL  # Вариант №1 считаем сумму сразу
            f.write(f"{VAL} ")
    # Вариант №1 считываем файл в строку, преобразуем в список, создаем через генератор список типом float,
    # создаем через генератор список типом float, считаем ссумму
    with open(file=FILENAME, mode="r", encoding="utf-8") as f:
        STR = f.read()
        FLOAT_LST = [float(ELEM) for ELEM in STR.split(" ") if ELEM != ""]
        SUM2 = sum(FLOAT_LST)
except IOError:
    print("Ошибка достапа к файлу")
except ValueError:
    print("Строка не является числом")
else:
    print(f"Ок.\nCумма: {SUM1:.3f}\nCумму, считывая файл : {SUM2:.3f}")
