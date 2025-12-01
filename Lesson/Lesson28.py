# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         # to todo
#         return result.upper()
#
#     return wrapper
#
#
# @uppercase_decorator
# def salom_ber(name):
#     return f"{name} salom!!!"
#
#
# print(salom_ber('Ali'))
# import datetime
import datetime


# now = datetime.datetime.now()
# print(now)


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        print()
#@timer
def summa(sonlar: list):
    now = datetime.datetime.now()

    total = 0
    for i in sonlar:
        total += i

    finished = datetime.datetime.now()
    print((finished - now).microseconds)
    return total


#@timer
def kopaytma(sonlar):
    now = datetime.datetime.now()
    total = 1
    for i in sonlar:
        total *= i
    finished = datetime.datetime.now()
    print((finished - now).microseconds)
    return total


print(summa([12, 24, 3434, 12]))
print(kopaytma([12, 24, 3434, 12]))

