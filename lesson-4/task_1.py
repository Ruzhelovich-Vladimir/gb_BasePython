"""
1. 	Реализовать скрипт, в котором должна быть предусмотрена
    функция расчета заработной платы сотрудника. В расчете
    необходимо использовать формулу: (выработка в часах *
    ставка в час) + премия. Для выполнения расчета для
    конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def convert_to_float(val):
    """
    Преобразование параметра в действительное число
    :param val: строка
    :return: действительное число
    """
    result = None
    try:
        result = float(val)
    except ValueError:
        print(f"Значение '{val}' не может быть преобразовано в действительное число!")

    return result


if len(argv) == 4:
    GET_SALARY = (lambda val, bonus, hour: hour * val + bonus)
    VAL, BONUS, HOUR = convert_to_float(argv[1]), \
                       convert_to_float(argv[2]), \
                       convert_to_float(argv[3])
    if None not in (VAL, BONUS, HOUR):
        print(f"Заработная плата составит: {GET_SALARY(VAL, BONUS, HOUR)} руб.")
else:
    print("Не хватает параметров, введите скрипт со следующими параметрами task_1 СтоимостьЧаса "
          "Перемия ОтработанныеЧасы")

"""
"C:\Program Files (x86)\Python38-32\python.exe" C:/Users/Vladimir/Desktop/GB_PythonBase/lesson-4/task_1.py 200 25000 200
Заработная плата составит: 65000.0 руб.
"""
