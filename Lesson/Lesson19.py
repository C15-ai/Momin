# polimorfizm
# librarytem
class Author:
    def __init__(self, full_name, bio):
        self.full_name = full_name
        self.bio = bio


class Book:
    def __init__(self, name, author, year, genre, dds_number, isbn):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.dds_number = dds_number
        self.isbn = isbn


class Catalog:
    def __init__(self, name):
        self.name = name
        self.books = []

    # def add_book(self, book):
    #     if isinstance(book, Book):
    #         self.books.append(book)
    #     else:
    #         print('Book classini obiyeti emas')
    def search_book(self, name):

            for i in self.books:
                if i.name.lower() == name.lower():
                    print(f" {i.name} kitobi mavjud. DDS raqami: {i.dds_number}")
                    return i
            print(f" {name} kitobi topilmadi.")
            return None


author1 = Author('Ibn Xaldun', """Ibn Xaldun Abduraxman Abu Zayd Ibn Muhammad (1332-yil 27-may, Tunis – 1406-yil 17-mart, Qohira) – arab tarixchisi va faylasufi. Ibn Rushdning izdoshi. 1349–1375-yillarda Tunis, Fes, Gʻarnota, Bujjoya (Jazoirda) hukmdorlari saroyida yuqori lavozimlarda ishlagan. 1382-yil Misrga kelib, mudarrislik qilgan, umrining oxirida molikiylar mazhabi qozisi boʻlgan.
""")
book1 = Book('Muqqadima', author1, 1389, 'siyosat', 2034, 1232323)
book2 = Book('Muqqadima2', author1, 1399, 'siyosat', 2035, 1232123)

#c1 = Catalog('1-catalog')


#
#  # c1.add_book(book1)
#  # c1.add_book(book2)
#  # c1.add_book('sariq dev')
#
# print(c1.search('Muqqadima'))
# def main():
#    while True:
#      #choice  = int(input('1.Kitoblar royxati\n2.kitob qoshish\n3.kitob qidirish\n4.Exit'))




