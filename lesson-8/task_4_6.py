"""
4)	Начните работу над проектом «Склад оргтехники». Создайте класс,
    описывающий склад. А также класс «Оргтехника», который будет базовым
    для классов-наследников. Эти классы — конкретные типы оргтехники
    (принтер, сканер, ксерокс). В базовом классе определить параметры,
    общие для приведенных типов. В классах-наследниках реализовать
    параметры, уникальные для каждого типа оргтехники.
5)	Продолжить работу над первым заданием. Разработать методы, отвечающие
    за приём оргтехники на склад и передачу в определенное подразделение
    компании. Для хранения данных о наименовании и количестве единиц
    оргтехники, а также других данных, можно использовать любую подходящую
    структуру, например словарь.
6)	Продолжить работу над вторым заданием. Реализуйте механизм валидации
    вводимых пользователем данных. Например, для указания количества
    принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь по возможности реализовать в проекте «Склад
    оргтехники» максимум возможностей, изученных на уроках по ООП.
"""


class FeatureError(Exception):
    """
    Класс исключения для характеристик оборудования
    """

    def __init__(self, feature_type):
        print(f"Не корректное значение характеристики {feature_type}")


class Warehouse:
    """Скласс Складов"""
    pass


class Equipment:
    """Класс Техники"""

    def __init__(self, **kwargs):
        """
        :param kwargs:
             "article": артикул
             "name": наименование
             "page_format": формат страницы
        """
        self.article = kwargs['article']
        self.name = kwargs['name']
        self.page_format = kwargs['page_format']

    def __str__(self):
        return f"{self.article} {self.name}"

    @staticmethod
    def check_int(value):
        """
        Проверка на целочисленное значение
        :param value: Параметр
        :return: Целочисленное число в противном случае сообщает об ошибке
        """

        if value.isdigit():
            return int(value)
        else:
            raise FeatureError("натуральное число")

        return result

    @staticmethod
    def check_type(obj_type, type_tuple):
        """
        :param obj_type: тип
        :param type_tuple: список с типами
        :return: Значение, если оно соответствует списку, в противном случае None
        """

        if obj_type in type_tuple:
            return obj_type
        else:
            raise FeatureError("тип характеристики")


class Printer(Equipment):
    """Класс Принтеров"""

    type_tuple = ('planshet', 'jet ', 'matrix', '3d')

    def __init__(self, **kwargs):
        """
        :param kwargs:
             "article": артикул
             "name": наименование
             "page_format": формат бумаги
             "type": тип ('planshet', 'jet ', 'matrix', '3d')
             "color_num": кол-во цветов
             "print_speed": скорость печати
             "cartridge_resource: ресурс картриджа в страницах
        """
        super().__init__(**kwargs)
        self.type = super().check_type(kwargs['type'], self.type_tuple)
        self.color_num = kwargs['color_num']
        self.print_speed = kwargs['print_speed']
        self.cartridge_resource = kwargs['cartridge_resource']


class Scanner(Equipment):
    """Класс Сканер"""

    type_tuple = ('digital_sender', 'drum', 'rotary', 'hand-held')

    def __init__(self, **kwargs):
        """
        :param kwargs:
             "article": артикул
             "name": наименование
             "page_format": формат бумаги
             "type": тип ('digital_sender', 'drum', 'rotary', 'hand-held')
             "dpi": разрешение (dpi)
             "color_bit": глубина цветов (в битах)
        """
        super().__init__(**kwargs)
        self.type = super().check_type(kwargs['type'], self.type_tuple)
        self.dpi = kwargs['dpi']
        self.color_bit = kwargs['color_bit']


class Copier(Printer, Scanner):
    """Класс Ксерокса - это по сути объеденение двух устройств принтера и сканера,
    поэтому я и сдалал данный класс потомком от двух классов
    """

    type_tuple = ('type1', 'type2', 'type3')

    def __init__(self, **kwargs):
        """
        :param kwargs:
             "article": артикул
             "name": наименование
             "page_format": формат бумаги
             "type": тип ('planshet', 'jet ', 'matrix', '3d')
             "color_num": кол-во цветов
             "print_speed": скорость печати
             "cartridge_resource: ресурс картриджа в страницах
             "dpi": разрешение (dpi)
             "color_bit": глубина цветов (в битах)
        """
        super().__init__(**kwargs)  # Инициализируем свойства классов родителей
        self.type = super().check_type(kwargs['type'], self.type_tuple)


class Warehouse:
    """Класс для складского учёта"""

    def __init__(self, name):
        """Констурктор"""
        self.name = name
        self.stocks = {}  # Формат {артикул, остаток}

    def take(self, good, count):
        """Оприходование"""

        if self.stocks.get(good.article, False) > 0:
            self.stocks[good.article] += count
        else:
            self.stocks[good.article] = count

    def move_to(self, good, count, warehouse):
        """
        перемещение с одного слада на другой.
        Решил сделать более универсальный метод перемещение на склад
        """

        if self.stocks[good.article] >= count:
            # Увеличиваем остатки складе приёмник
            warehouse.take(good, count)
            # Уменьшаем на остатки складе источника
            self.stocks[good.article] -= count
            print(
                f"Передача товара '{good.name}' на склад '{warehouse.name}' - ОК")
        else:
            print("Не возможно переместить товар, которого нет на данном складе.")

    def __str__(self):
        """преобразуем в строку"""
        result = f"Остатки на складе {self.name}:"
        for key, value in self.stocks.items():
            result = f"{result}\n{key:10}:{value}"
        return result


GOOD1 = Copier(article="Xerox",
               name="Brother 3070",
               page_format="A4",
               type="type1",
               color_num=100000,
               print_speed=20,
               cartridge_resource=30000,
               dpi=24,
               color_bit=64)

GOOD2 = Scanner(
    article="Scan",
    name="HP ScanJet 3020",
    page_format="A4",
    type="digital_sender",
    dpi=128,
    color_bit=32)

WAREHOUSE1 = Warehouse("Основной склад")
WAREHOUSE2 = Warehouse("Бухгалтерия")

WAREHOUSE1.take(GOOD1, 2)
WAREHOUSE1.take(GOOD2, 2)
print(f"Остатки '{WAREHOUSE1.name}':{WAREHOUSE1.stocks}")
print(f"Остатки '{WAREHOUSE2.name}':{WAREHOUSE2.stocks}")
WAREHOUSE1.move_to(GOOD1, 1, WAREHOUSE2)
WAREHOUSE1.move_to(GOOD2, 1, WAREHOUSE2)
print(f"Остатки '{WAREHOUSE1.name}':{WAREHOUSE1.stocks}")
print(f"Остатки '{WAREHOUSE2.name}':{WAREHOUSE2.stocks}")
