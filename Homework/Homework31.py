def foo():
    print("begin")
    for i in range(3):
        print("Yeild oldin")
        yield i
        print("Yeild keyin", i)
    print("end")

f = foo()

print(next(f))
print(next(f))
print(next(f))
print(next(f))

