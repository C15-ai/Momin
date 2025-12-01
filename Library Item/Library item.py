import logging
import pickle
from logging import critical
from re import search

logging.basicConfig(
    level=logging.ERROR,
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug("Logging ishga tushdi") #dubug1
logging.info("Logging dasturdagi parementlar ishlayapt") #info1
logging.warning("Dastur ishga tushmoqda") #warning1

def write_data(data):
    logging.debug("Writing data funksiyasi caqrildi")
    with open('library.dat', 'wb') as f:
        pickle.dump(data, f)


def read_data():
    try:
        with open('library.dat', 'rb') as f:
            data = pickle.load(f)
        return data
    except:
        logging.error(f"eror{f}") #eror2
        return None
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject
    logging.debug("Library item clasi ishlayapti") #debug2
    @abstractmethod
    def locate(self):
        pass

    def __str__(self):
        return f"Kitob nomi:{self.title} upc: {self.upc} mavzusi: {self.subject}"


class Book(LibraryItem):
    def __init__(self, title, upc, subject, isbn, dds_number):
        super().__init__(title, upc, subject)
        self.isbn = isbn
        self.dds_number = dds_number

    def locate(self):
        return self.dds_number
    logging.debug("book klasi abstractmethod ni ishlatdi") #debug3
    def __str__(self):
        return f"Kitob nomi:{self.title} isbn: {self.isbn} dds raqami: {self.dds_number}"


class Magazine(LibraryItem):
    def __init__(self, title, upc, subject, volume, son):
        super().__init__(title, upc, subject)
        self.volume = volume
        self.son = son

    def locate(self):
        return self.volume

    def __str__(self):
        return f"Jurnal nomi:{self.title} volume: {self.volume} Son: {self.son}"


class DVD(LibraryItem):
    def __init__(self, title, upc, subject, actors, director, ganre):
        super().__init__(title, upc, subject)
        self.actors = actors
        self.director = director
        self.ganre = ganre


    def locate(self):
        return f"Janri {self.ganre}"

    def __str__(self):
        return f"DVD: {self.title} actors: {self.actors} director: {self.director}"


class CD(LibraryItem):
    def __init__(self, title, upc, subject, artist):
        super().__init__(title, upc, subject)
        self.artist = artist

    def locate(self):
        return f"Artist: {self.artist}"

    def __str__(self):
        return f"CD: {self.title} artist: {self.artist}"


class Catalog:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.items.append(item)
        logging.info(f"catalogga qoshildi {item.title}") #info2

    def get_list(self):
        return self.items

    def search(self, title):

        for i in self.items:
            if i.title.lower() == title.lower():
                logging.info(f"topildi {title}")
                return i

        logging.error("Topilmadi") #eror1
        return None

    def faylga_saqlash(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self.items, f)
            logging.info(f"Catalog faylga yuklandi {filename}") #info3
        except Exception as e:
            logging.critical(f"faylga saqlashda xatolik: {e}") #critical1

    def fayl_oqish(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.items = pickle.load(f)
            logging.info(f"Katalog yuklandi: {f}") #info3
        except FileNotFoundError as f:
            logging.warning("Katalog fayli topilmadi ")  #warning2
        except ValueError as f:
            logging.critical(f"Yuklashda  xatolik: {filename}") #critical2

def main():
    data = read_data()
    if data:
        c1 = data
    else:
        c1 = Catalog('1-katalog')
        write_data(c1)

    c1 = Catalog("1-catalog")
    c1.add_item(Book("Shaytanat", 12345, "Detektiv", 3333, 12345111))
    c1.add_item(Magazine("FBO", 54321, "National", "Vol.10", "No.5"))
    c1.add_item(DVD("Iterstellar", 11111, "Hayotiy", "Mateo Mokkoni, Jesikka Chesteyn", "Christopher Nolan", "Triller"))
    c1.add_item(CD("Tuz Krall", "22222", "Music", "Cem Adrian"))
    while True:
        print("===MENU===")
        print("1.Menuni Korish")
        print("2.Kitoblar")
        print("3.Jurnallar")
        print("4.DVDlar")
        print("5.CD lar")
        print("6.Kitob qoshish")
        print("7.Jurnal qoshish")
        print("8.DVD qoshish")
        print("9.CD qoshish")
        print("10.Qidirish")
        print("11.EXIT")
        try:
            choice = int(input("Tanlang"))

        except ValueError:
            logging.critical(f"Foydalanuvci son kritmadi") #critical3


            print("Xatolik:Faqat son kriting")
            continue
        if choice == 1:
            a = c1.get_list()
            if not a:
                print("Ro1yxat bosh")
            else:
                for item in a:
                    print(item)
        elif choice == 2:
            for item in c1.items:
                if isinstance(item, Book):
                    print(item)
        elif choice == 3:
            for item in c1.items:
                if isinstance(item, Magazine):
                    print(item)
        elif choice == 4:
            for item in c1.items:
                if isinstance(item, DVD):
                    print(item)
        elif choice == 5:
            for item in c1.items:
                if isinstance(item, CD):
                    print(item)
        elif choice == 6:
            print("Malumatlarni kriting")
            title = input("Kitob nomi")
            upc = input("UPC")
            subject = input("Mavzusi")
            isbn = input("ISBN")
            dds_number = input("DDS Number")
            c1.add_item(Book(title, upc, subject, isbn, dds_number))
            print("kitob qoshildi")
        elif choice == 7:
            print("Malumotlarni kriting")
            title = input("Jurnal nomi")
            upc = input("UPC")
            subject = input("Mavzusi")
            volume = input("Jildi")
            son = input("Soni")
            c1.add_item(Magazine(title, upc, subject, volume, son))
        elif choice == 8:
            print("Malumotlarni kriting")
            title = input("DVD nomi")
            upc = input("UPC")
            subject = input("Mavzusi")
            actors = input("Aktyorlari")
            director = input("Rejisiori")
            ganre = input("Janri")
            c1.add_item(DVD(title, upc, subject, actors, director, ganre))
        elif choice == 9:
            print("Malumotlarni kriting")
            title = input("CD nomi")
            upc = input("UPC")
            subject = input("Mavzusi")
            artist = input("Qoshiqcisi")
            c1.add_item(CD(title, upc, subject, artist))

        elif choice == 10:
            q = input("Qidiriliyotgan nom: ")
            result = c1.search(q)
            if result:
                print("Topildi:", result, "Joyi:", result.locate())
            else:
                print("Topilmadi")

        elif choice == 11:
            print("Dastur tugadi.Etiboringiz uchun raxmat")
            break
        else:
            print("Notogri tanlov")
        if choice not in range(1, 12):
            logging.warning("Mavjud bo‘lmagan menu tanlandi") #warning3
            continue



main()
write_data("Asalom alekum")


