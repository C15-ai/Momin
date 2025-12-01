class Shaxs:
    def __init__(self, ism, yosh, jins):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins

    def __str__(self):
        return f"Ismi: {self.ism}, yoshi: {self.yosh}, jinsi: {self.jins}"

    def __repr__(self):
        return f"Ismi={self.ism}, yoshi= {self.yosh}, jinsi= {self.jins}"

    def __add__(self, other):
        return self.yosh + other.yosh

    def __eq__(self, other):
        return self.yosh == other.yosh and self.jins == other.jins

    def __lt__(self, other):
        return self.yosh < other.yosh

    def __getitem__(self, index):
        return self.ism[index]

    def __call__(self):
        return self.ism


a1 = Shaxs("Ali", 23, "Erkak")
b1 = Shaxs("Vali", 25, "Erkak")
c1 = Shaxs("Laylo",25, "Ayol")
print(a1)
print(b1)
print(repr(b1))
print(a1 + b1)
print(a1[0])
print(a1[1])
print(a1[2])
print(a1())
print(a1==b1)
print(b1==c1)
print(a1<b1)
print(a1>b1)
print(a1>c1)
print(a1())

