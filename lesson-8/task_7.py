"""
7)	Реализовать проект «Операции с комплексными числами». Создайте класс
    «Комплексное число», реализуйте перегрузку методов сложения и умножения
    комплексных чисел. Проверьте работу проекта, создав экземпляры класса
    (комплексные числа) и выполнив сложение и умножение созданных
    экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    """Класс комплексный чисел"""
    __slots__ = ('real_number', 'odd_number')

    def __init__(self, real_number=0, odd_number=0):
        """
        :param real_number: действительное число
        :param odd_number: мнимое число
        """
        self.real_number = float(real_number)
        self.odd_number = float(odd_number)

    def __str__(self):
        """текстовое представление"""

        real_str = f"{self.real_number}" if self.real_number != 0 else ""
        odd_str = f"{' + ' if len(real_str) > 0 else ''}" \
                  f"{self.odd_number}j" if self.odd_number > 0 else \
            f" - {self.odd_number}j" if self.odd_number < 0 else ""

        return f"{real_str}{odd_str}"

    def __add__(self, other):
        """Сложение"""
        return Complex(self.real_number + other.real_number,
                       self.odd_number + other.odd_number)

    def __mul__(self, other):
        """умножение"""

        return Complex(
            self.real_number * other.real_number -
            self.odd_number * other.odd_number,
            self.real_number * other.odd_number +
            self.odd_number * other.real_number)


print(f"{Complex(2) + Complex(2, 1)} - тест {complex(2) + complex(2, 1)}")
print(f"{Complex(2, 3) * Complex(2, 2)} - тест {complex(2, 3) * complex(2, 2)}")
print(f"{Complex(2, 2) * Complex(2, 2)} -тест {complex(2, 2) * complex(2, 2)}")
