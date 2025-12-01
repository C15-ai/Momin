1
class Car:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f'{self.brand} {self.model} {self.year}'
class Electrocar(Car):
    def __init__(self, brand,model,year,battery_capacity):
        super().__init__(brand,model,year)
        self.battery_capacity = battery_capacity
class Hybridcar(Car):
    def __init__(self, brand,model,year,fuel_tank,battery_capacity):
        super().__init__(brand,model,year)
        self.fuel_tank = fuel_tank
        self.battery_capacity = battery_capacity
c1=Car('Chevrolet','Malibu',2024)
e1=Electrocar('Tesla','Model S',2024,100)
h1=Hybridcar('Toyota','Prius',2024,43,45)
print(h1.battery_capacity)
print(h1.fuel_tank)
#2
class Hause:
    def __init__(self,adress,maydoni,narxi):
        self.adress = adress
        self.maydoni = maydoni
        self.narxi = narxi
    def get_info(self):
        return f"{self.adress} {self.maydoni} {self.narxi}"
class Luxury_hause(Hause):
    def __init__(self,adress,maydoni,narxi,basseyn):
        super().__init__(adress,maydoni,narxi)
        self.basseyn = basseyn
class Kop_qavatli_uy(Hause):
    def __init__(self,adress,maydoni,narxi,qavati):
        super().__init__(adress,maydoni,narxi)
        self.qavati = qavati
h1=Hause('Yunsobod',120,50000000)
l1=Luxury_hause('yunsobod',120,50000000,'basseyn')
k1=Kop_qavatli_uy('Mirzo ulugbek',60,50000,9)
print(h1.adress)
print(h1.get_info())
print(l1.get_info())
