"""
3)	Реализовать базовый класс Worker (работник), в котором определить
    атрибуты: name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например,
    {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
    на базе класса Worker. В классе Position реализовать методы
    получения полного имени сотрудника (get_full_name) и дохода с
    учетом премии (get_total_income). Проверить работу примера на
    реальных данных (создать экземпляры класса Position, передать
    данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """
    Родительский класс
    """

    __slots__ = ('name', 'surname', 'position', '_income')

    def __init__(self, **kwargs):
        """
        :param name: имя
        :param surname: фамилия
        :param position: должность
        :param wage: оклад
        :param bonus: премия
        """
        self.name, self.surname, self.position, self._income = \
            kwargs["name"], kwargs["surname"], kwargs["position"], \
            {"wage": kwargs["wage"], "bonus": kwargs["bonus"]}


class Position(Worker):
    """
    Дочерний класс
    """

    def get_full_name(self):
        """
        :return: полное имя сотрудника
        """
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        """
        :return: доход
        """

        return self._income["wage"] + self._income["bonus"]


PERSONAL = Position(name="Владимир",
                    surname="Ружелович",
                    position="программист",
                    wage=70000,
                    bonus=35000)
print(f"ФИО {PERSONAL.get_full_name()}; "
      f"должность - {PERSONAL.position}; "
      f"доход - {PERSONAL.get_total_income()}")
