# normativ 10
from abc import ABC, abstractmethod


class Computer(ABC):
    total_computers = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        Computer.total_computers += 1

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def  get_total_computers(cls):
        return Computer.total_computers


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, scren_size):
        super().__init__(brand, model, year, price)
        self.scren_size = scren_size

    def display_info(self):
        print(
            f"Monoblock-{self.brand}. Modeli-{self.model}. Ishlab cqarilgan yili-{self.year}. Ekrani-{self.scren_size}. Narxi-{self.price} $")


class Notebook(Computer):
    def __init__(self, brand, model, year, price, batery_life):
        super().__init__(brand, model, year, price)
        self.batery_life = batery_life

    def display_info(self):
        print(
            f"Notebook-{self.brand}. Modeli-{self.model}. Ishlab cqarilgan yili-{self.year}. Batereya sgimi-{self.batery_life}. Narxi-{self.price} $")


m1 = Monoblock("Apple", "Imac", 2022, 1500, 27)
n1 = Notebook("Huawei", "d14", 2023, 1000, 12)
m1.display_info()
n1.display_info()
print(f'Jami Campyuterlar {Computer.total_computers} ')
