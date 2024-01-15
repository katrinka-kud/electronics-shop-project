from src.item import Item


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
            raise Exception('C объектами других классов запрещено сложение.')


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
