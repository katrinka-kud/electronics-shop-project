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

        try:
            with open(filename, 'r', encoding='windows-1251', newline='') as f:
                reader = csv.DictReader(f)
                for line in reader:
                    name = line['name']
                    price = float(line['price'])
                    quantity = int(line['quantity'])
                    if list(line.keys()) != ['name', 'price', 'quantity']:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    else:
                        cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')


class InstantiateCSVError(Exception):

    def __init__(self, *args):
        print('InstantiateCSVError: Файл item.csv поврежден')

    def __str__(self):
        return 'InstantiateCSVError: Файл item.csv поврежден'
