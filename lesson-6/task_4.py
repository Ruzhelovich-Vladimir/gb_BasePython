"""
4)	Реализуйте базовый класс Car. У данного класса должны быть
    следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать,
    что машина поехала, остановилась, повернула (куда). Опишите
    несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
    . Добавьте в базовый класс метод show_speed, который должен
    показывать текущую скорость автомобиля. Для классов TownCar и
    WorkCar переопределите метод show_speed. При значении скорости
    свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
    о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат. Выполните
    вызов методов и также покажите результат.
"""


class Car:
    """
    Базовый класс автомашин
    """
    __slots__ = ('speed', 'color', 'name', 'is_police', 'car_type')

    def __init__(self, name, color, speed):
        self.speed, self.color, self.name, self.is_police, self.car_type = speed, color, name, True, None

    def go(self):
        """
        Сообщает, что автомобиль находиться в движении
        """
        print(f"{self.car_type}:Автомобиль {self.name} ({self.color}) находиться в движении.")

    def stop(self):
        """
        Сообщает, что автомобиль остатновился
        """
        print(f"{self.car_type}:Автомобиль {self.name} ({self.color}) остановился.")

    def turn(self, direction):
        """
        Сообщает, что автомобиль повернул
        :return:
        """
        print(f"{self.car_type}:Автомобиль {self.name} ({self.color}) повернул {direction}")

    def show_speed(self):
        """
        Показывает текущую скорость
        :return:
        """
        print(f"{self.car_type}:Текущая скорость автомобиль {self.name} ({self.color}) "
              f"- {self.speed} км/ч")


class TownCar(Car):
    """
    Класс городского автомобиля
    """

    def __init__(self, name="Nissan", color="white", speed=60):
        super().__init__(name, color, speed)
        self.is_police = False
        self.car_type = "городской автомобиль"

    def show_speed(self):
        super().show_speed()

        if self.speed > 60:
            print(f"{self.car_type}:Вы привышаете скорость!!!")


class SportCar(Car):
    """
    Класс спортивного автомобиля
    """

    def __init__(self, name="Nissan", color="white", speed=65):
        super().__init__(name, color, speed)
        self.is_police = False
        self.car_type = "спортивный автомобиль"


class WorkCar(Car):
    """
    Класс рабочего автомобиля
    """

    def __init__(self, name="Nissan", color="white", speed=40):
        super().__init__(name, color, speed)
        self.is_police = False
        self.car_type = "рабочий автомобиль"

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.car_type}:Вы привышаете скорость!!!")


class PoliceCar(Car):
    """
    Класс автомобиля полицейского
    """

    def __init__(self, name="Nissan", color="white", speed=65):
        super().__init__(name, color, speed)
        self.is_police = True
        self.car_type = "полицейский автомобиль"

print("*"*50)
CAR1 = TownCar()
CAR1.go()
CAR1.turn("налево")
CAR1.show_speed()
CAR1.stop()
print("*"*50)
CAR1 = TownCar("Nissan", "Red", 65)
CAR1.go()
CAR1.turn("налево")
CAR1.show_speed()
CAR1.stop()
print("*"*50)
CAR2 = SportCar()
CAR2.go()
CAR2.turn("налево")
CAR2.show_speed()
CAR2.stop()
print("*"*50)
CAR3 = WorkCar()
CAR3.go()
CAR3.turn("налево")
CAR3.show_speed()
CAR3.stop()
print("*"*50)
CAR3 = WorkCar("Nissan", "Red", 45)
CAR3.go()
CAR3.turn("налево")
CAR3.show_speed()
CAR3.stop()
print("*"*50)
CAR4 = PoliceCar()
CAR4.go()
CAR4.turn("налево")
CAR4.show_speed()
CAR4.stop()
