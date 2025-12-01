class Auto:
    __auto_number = 0
    def __init__(self,model,rang,karobka,narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        Auto.__auto_number += 1
    def get_info(self):
        return f"{self.rang} rangli {self.model} narxi {self.narh} $"
    @classmethod
    def get_auto_number(cls):
        return cls.__auto_number
a1=Auto("Malibu","Qora","Avtomat",25000)
print(a1.get_info())
print(a1.get_auto_number())




