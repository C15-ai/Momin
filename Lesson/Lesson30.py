def split(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.split(" ")

    return wrapper
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@split
@uppercase
def slaom_ber(massage):
    return f"Salom {massage}"


print(slaom_ber("Ali"))
