#11normotiv
from abc import ABC, abstractmethod


class Computer(ABC):
    total_computers = 0

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price = price
        Computer.total_computers += 1

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Xatolik:Faqat musbat qiymat kriting")

    def __gt__(self, other):
        return self.__price > other.year

    def __repr__(self):
        return f"{self.__class__.__name__}: Brand={self.brand},Model= {self.model},Ishlab cqarilgan yili= {self.year}"

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computers(cls):
        return Computer.total_computers


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, scren_size):
        super().__init__(brand, model, year, price)
        self.scren_size = scren_size

    def display_info(self):
        print(
            f"Monoblock-{self.brand}. Modeli-{self.model}. Ishlab cqarilgan yili-{self.year}. Ekrani-{self.scren_size}. Narxi-{self.__price} $")


class Notebook(Computer):
    def __init__(self, brand, model, year, price, batery_life):
        super().__init__(brand, model, year, price)
        self.batery_life = batery_life

    def display_info(self):
        print(
            f"Notebook-{self.brand}. Modeli-{self.model}. Ishlab cqarilgan yili-{self.year}. Batereya sgimi-{self.batery_life}. Narxi-{self.__price} $")


class Factory:
    total_factories = 0

    def __init__(self, name):
        self.name = name
        self.products = []
        Factory.total_factories += 1

    def add_product(self, product):
        if isinstance(product, Computer):
            self.products.append(product)
            print(f"{product.model} {self.name} zavodiga qoshildi")
        else:
            print("Xatolik:Faqat kampyuter elementlari qabul qlinadi")

    def list_products(self):
        for i in self.products:
            print(i)

    def get_total_factories(cls):
        return cls.total_factories


m1 = Monoblock("Apple", "Imac", 2022, 1500, 27)
n1 = Notebook("Huawei", "d14", 2023, 1000, 12)
n2 = Notebook("HP", "Envy", 2024, 1000, 12)
m2 = Monoblock("Pokerd bell", "h", 2012, 500, 21)
#m1.display_info()
#n1.display_info()
print(f'Jami Campyuterlar {Computer.total_computers}')
f1 = Factory("Zavod 1")
f2 = Factory("Zavod 2")
f1.add_product(n1)
f2.add_product(m1)
f2.add_product(m2)
f1.add_product(n2)
print("Zavod 1 mahsulotlari")
f1.list_products()
print("Zavod 2 mahsulotlari")
f2.list_products()
print(f"Jami Zavodlar {Factory.total_factories}")
n1.set_price(1100)
print(n1.get_price())
