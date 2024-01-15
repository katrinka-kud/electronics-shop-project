import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)


    def __repr__(self) -> str:
        return f'Имя: {self.name}, цена: {self.price}'

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(digit: str) -> int:
        return int(float(digit))

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv') -> None:
        """
        Загружает данные из csv файла и преобразует их в список словарей
        """
        cls.all.clear()

        with open(filename, 'r', encoding='UTF-8', newline='') as f:
            reader = csv.DictReader(f)
            for line in reader:
                name = line['name']
                price = float(line['price'])
                quantity = int(line['quantity'])
                cls(name, price, quantity)


class Phone(Item):
    def __init__(self,
                 name: str,
                 price: float,
                 quantity: int,
                 number_of_sim: int):
        super().__init__(name, price, quantity)
        if number_of_sim > 0 and isinstance(number_of_sim, int):
            self.__number_of_sim = number_of_sim
        else:
            raise AttributeError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}, {self.quantity}, {self.__number_of_sim}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise (Exception('C объектами других классов запрещено сложение.'))


class Mixin():
    def __init__(self, *args, **kwargs):
        language = 'EN'
        super().__init__(*args, **kwargs)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self.__language
        elif self.__language == 'RU':
            self.__language = 'EN'
            return self.__language


class Keyboard(Mixin, Item):
    def __init__(self, *args):
        super().__init__(*args)
