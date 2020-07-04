"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь
    определенное название. К типам одежды в этом проекте относятся пальто и
    костюм. У этих типов одежды существуют параметры: размер (для пальто) и
    рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

    Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
    методов на реальных данных.

    Реализовать общий подсчет расхода ткани. Проверить на практике полученные
    на этом уроке знания: реализовать абстрактные классы для основных классов
    проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractclassmethod


class Clothes(ABC):
    """
    Обстрактный класс одежды Clothes
    """

    def __init__(self, name):
        """
        Конструктор класса
        :param name: Наименовании одежды
        """
        self.name = name


class Coat(Clothes):
    """
    Класс товара "Пальто"
    """

    def __init__(self, name, size):
        """
        Конструктор дочернего класса
        :param name: наименование
        :param size: размер
        """
        super().__init__(name)
        self.V = size

    def __setattr__(self, attr, value):
        """
        :param attr: атрибут
        :param value: значение
        :return:
        """
        # Не очень красиво реализовал, т.к. при каждой итерации сетора вызывается,
        # сеттер родительского класса, позже поэксперементирую
        super().__setattr__(attr, value)
        if attr == "V":
            self.__dict__[attr] = value if 40 < value < 55 else 46
        # else:
        #    super().__setattr__(attr, value)
        # НЕ СМОГ РАЗОБРАТЬСЯ ПОЧЕМУ ТАК НЕ РАБОТАЕТ

    @property
    def tissue(self):
        """
        :return: Расход ткани
        """
        return self.V/6.5 + 0.5

class Costume(Clothes):

    def __init__(self, name, size):
        """
        Конструктор дочернего класса
        :param name: наименование
        :param size: размер
        """
        super().__init__(name)
        self.H = size

    def __setattr__(self, attr, value):
        """
        :param attr: атрибут
        :param value: значение
        :return:
        """
        # Не очень красиво реализовал, т.к. при каждой итерации сетора вызывается,
        # сеттер родительского класса, позже поэксперементирую
        super().__setattr__(attr, value)
        if attr == "H":
            self.__dict__[attr] = value if 100 < value < 210 else 176
        # else:
        #    super().__setattr__(attr, value)
        # НЕ СМОГ РАЗОБРАТЬСЯ ПОЧЕМУ ТАК НЕ РАБОТАЕТ

    @property
    def tissue(self):
        """
        :return: Расход ткани
        """
        return 2 * self.H + 0.3


CLOTHES = Coat("пальто", 0)
print(f"На {CLOTHES.name} (раз. {CLOTHES.V}) требуется {CLOTHES.tissue:.3f}")

CLOTHES = Costume("костюм", 0)
print(f"На {CLOTHES.name} (рост {CLOTHES.H}) требуется {CLOTHES.tissue:.3f}")
