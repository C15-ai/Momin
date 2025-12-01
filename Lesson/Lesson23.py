from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject

    @abstractmethod
    def locate(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, upc, subject, isbn, dds_number):
        super().__init__(title, upc, subject)
        self.isbn = isbn
        self.dds_number = dds_number

    def locate(self):
        return self.dds_number

    # def __str__(self):
    #     return f'{self.title}, {self.upc}, {self.subject} '

    def __repr__(self):
        return f'{self.title}, {self.upc}, {self.subject} '


class Catalog:
    def __init__(self, name):
        self.name = name
        self.item = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.item.append(item)

    def get_item(self):
        pass

    def search(self, title):
        pass

    def __add__(self, other):
        new_catalog = Catalog(f'{self.name}&{other.name}')
        new_catalog.item = self.item + other.item
        return new_catalog

    def __len__(self):
         return len(self.item)

    def __gt__(self, other):
         return len(self.item)>len(other.item)
    def __lt__(self,other):
         return len(self.item)<len(other.item)
    def __eq__(self, other):
         return len(self) == len(other)
    def __call__(self, *args, **kwargs):
         return self.item
    def __setitem__(self,key,value):
        self.item[key] = value


book = Book('Kitob', '12', 'nimadir', 'adsdas', 1221212)
book2 = Book('Kitob2', '12', 'nimadir', 'adsdas', 1221212)
book3 = Book('Kitob', '12', 'nimadir', 'adsdas', 1221212)

c1 = Catalog('1-catalog')
c2 = Catalog('2-catalog')

c1.add_item(book)
c2.add_item(book2)

c3 = c1 + c2

# print(c3 > c1)  # True
# print(c3 < c1)  # True
# print(c3 < c2)
# print(c3==c1


# print(c3.name)
# print(c3.item)
# print(len(c3))

# a = '12'
# b = '13'
# print(a+b)

# len('salom')  # 5
# len([1, 2, 3])  # 3

# print([1, 2] + [3, 4]) # [1,2,3,4]
print(c3)
