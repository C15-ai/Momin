import logging
import datetime
logging.basicConfig(
    filename="factory_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# --- Dekorator ---
def log_decorator(level=logging.INFO):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.log(level, f"{func.__name__} muvaffaqiyatli bajarildi.")
                if isinstance(result, str):
                    logging.info("result ishladi")
                    logging.log(level, f'{func.__name__} chaqirildi.')
                else:
                    logging.log(level, f'{func.__name__} chaqirildi.')
                return result
            except Exception as e:
                logging.error(f"Xatolik: {func.__name__} - {str(e)}")
        return inner
    return wrapper

# --- Klasslar ---
class Computer:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self._price = price
    @log_decorator()
    def display_info(self):
        return f'INFO: {self.brand} {self.model} ({self.year}), narx: {self._price}'
    @log_decorator()
    def set_price(self, new_price):
        if new_price < 0:
            return "WARNING: narx manfiy bo'lishi mumkin emas"
        self._price = new_price
        return "INFO: narx o'zgartirildi"

class Factory:
    total_factories = 0
    def __init__(self, name):
        self.name = name
        self.products = []
        Factory.total_factories += 1
    @log_decorator('INFO')
    def add_product(self, product):
        # ERROR/INFO natija orqali
        if isinstance(product, Computer):
            self.products.append(product)
            return "INFO: mahsulot qo'shildi"
        return "ERROR: noto'g'ri obyekt qo'shishga urinish"
    @log_decorator('INFO')
    def list_products(self):
        # Konsolga chiqarish - o'qituvchi ko'rishi uchun
        for p in self.products:
            print(p.display_info())
        return "INFO: ro'yxat chiqarildi"
    @classmethod
    def get_total_factories(cls):
        return cls.total_factories

# --- Sinov ---
pc1 = Computer('Lenovo', 'ThinkPad', 2021, 900)
pc2 = Computer('Lenovo', 'ThinkPad', 2021, 900)

print(pc1.display_info())
print(pc2.display_info())
print(pc2.set_price(950))    # INFO
print(pc2.set_price(-200))   # WARNING
f1 = Factory('Toshkent zavodi')
print(f1.add_product(pc1))   # INFO
print(f1.add_product('xato')) # ERROR
print(f1.list_products())

print("Jami zavodlar:", Factory.get_total_factories())
