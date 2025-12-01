#1
def only_positive(func):
    def wrapper(num):
        if num < 0:
            return "Xatolik faqat musbat son kriting"
        return func(num)

    return wrapper


@only_positive
def square(num):
    return num ** 2


print(square(5))
print(square(-3))


#2
def caunt_calls(func):
    caunt = 0

    def wrapper():
        nonlocal caunt
        caunt += 1
        print(f"{caunt} martta caqrildi")
        return func()

    return wrapper


@caunt_calls
def hello():
    print("hello world")


hello()
hello()


#3
def admin_only(func):
    def wrapper(user_id, **kwargs):
        if kwargs.get("role") == "admin":
            return func(f"ruxsat yoq ")
        return func(user_id, **kwargs)

    return wrapper


@admin_only
def delate_user(user_id, **kwargs):
    print(f"Foydalanuvci {user_id} muvafqiyatli ocrild")


delate_user(101, role="admin")
delate_user(102, role="user")
#4
from datetime import datetime
def time_restricted(start_hour, end_hour):
    def decorator(func):
        def wrapper():
            now = datetime.now().hour
            if start_hour < now < end_hour:
                return func()
            else:
                return "Hozir vaqt mos emas!"
        return wrapper
    return decorator


@time_restricted(9, 17)
def send_report():
    print("Hisobot muvaffaqiyatli yuborildi!")
print(send_report())
#5
def call_limit(limit):
    def decorator(func):
        count = 0
        def wrapper():
            nonlocal count
            if count >= limit:
                return "Funksiya caqruv limiti oshrildi"
            count += 1
            return func()
        return wrapper
    return decorator
@call_limit(5)
def proces_data():
    print("Malumotlar qayta ishlanmoqda")
proces_data()
proces_data()
proces_data()
proces_data()
print(proces_data())

