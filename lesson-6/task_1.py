"""
1)	Создать класс TrafficLight (светофор) и определить у него один
    атрибут color (цвет) и метод running (запуск). Атрибут реализовать
    как приватный. В рамках метода реализовать переключение светофора
    в режимы: красный, желтый, зеленый. Продолжительность первого состояния
    (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
    (зеленый) — на ваше усмотрение.  Переключение между режимами должно
    осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов, и при
    его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import turtle
from time import sleep

"""
Т.е. не ограничивали инструментами решил вспомнить библиотеку turtle,
использую её т.к. она является встроенной

Немного не красиво сделал выход, через исключение.
"""


class TrafficLight:
    """
    Класс демонстрации работы светофора
    """
    _index_total = None  # Текущий индекс цвета
    _colors = None  # Массив словарей с данными по режиму работы и характеристиками цвета

    def __init__(self, start_x=50, start_y=50, radius=25):
        """
        :param start_x: координата х
        :param start_y: координата y
        :param radius: радиус
        """
        self._index_total = 0
        self.__step = 1

        self._colors = [
            {"color": 'red',
             "wait": 7,
             "coordinates": (start_x, start_y),
             "radius": radius},
            {"color": 'yellow',
             "wait": 2,
             "coordinates": (start_x, start_y - radius * 2),
             "radius": radius},
            {"color": 'green',
             "wait": 7,
             "coordinates": (start_x, start_y - radius * 4),
             "radius": radius},
        ]
        self.__show()

    def __show(self):
        """
        Отображение сфетофора и текущего его состояния
        """
        turtle.hideturtle()
        turtle.speed(0)
        turtle.up()

        # Отрисовываю светофор, можно было конечно не весь светофор отрисовывать, но
        # не стал заморачиваться при решении этой задачи
        for inx, circle in enumerate(self._colors):
            if self._index_total == inx:
                turtle.color(circle["color"])
            else:
                turtle.color("gray")
            turtle.goto(circle["coordinates"][0], circle["coordinates"][1])
            turtle.down()
            turtle.begin_fill()
            turtle.circle(circle["radius"])
            turtle.end_fill()
            turtle.up()

        sleep(self._colors[self._index_total]["wait"])

    def next(self):
        """
        Смена режима сфетофра и его отображение
        """
        # Проверяем условие для смены направления движения цвета
        if self._index_total == 2:
            self.__step = -1
        elif self._index_total == 0:
            self.__step = 1

        # Изменяем текущий цвет
        self._index_total += self.__step
        # Отрисовываем светофор
        self.__show()


TL = TrafficLight(30, 30, 70)
try:
    for _ in range(20):
        TL.next()
except turtle.Terminator:
    print("Выход")
