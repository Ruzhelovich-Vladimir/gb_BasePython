"""
1)	Реализовать класс «Дата», функция-конструктор которого должна
    принимать дату в виде строки формата «день-месяц-год». В рамках
    класса реализовать два метода. Первый, с декоратором @classmethod,
    должен извлекать число, месяц, год и преобразовывать их тип к
    типу «Число». Второй, с декоратором @staticmethod, должен
    проводить валидацию числа, месяца и года (например, месяц —
    от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """Класс даты (Date)"""

    def __init__(self, date_str):
        """
        :param date_str: Строка формата «ДД-ММ-ГГГГ»
        """

        self.date_tuple = Date.get_date_tuple(date_str, "-")

    def __str__(self):
        """Текстовое представление числа"""
        return f"День: {self.date_tuple[0]};" \
               f"Месяц: {self.date_tuple[1]};" \
               f"Год: {self.date_tuple[2]}"

    @classmethod
    def get_date_tuple(cls, string, sep="-"):
        """Извлечение чисел из строковой переменной в кортеж"""
        try:
            # Получаем кортеж и сразу проверяем его влидность
            result = Date.check_date_tuple(
                tuple(int(elem) for elem in string.split(sep)))
        except ValueError:
            print("Не корректное значение числа")

        return result

    @staticmethod
    def check_date_tuple(date_tuple):
        """Валидация кортежа даты"""

        if not 1 <= date_tuple[0] <= 31:
            print(f"Не корректное значение дней - {date_tuple[0]}")
        if not 1 <= date_tuple[1] <= 12:
            print(f"Не корректное значение месяца - {date_tuple[1]}")

        return date_tuple


print(Date(input("Введите дату в формате 'ДД-ММ-ГГГГ': ")))
