#1Auto klasi
class Auto:
    def __init__(self,model,rang,karobka,narx,yil,kilometr=0):
        self.model = model
        self.rang = rang
        self.narx = narx
        self.yil = yil
        self.kilometr = kilometr
    def get_info(self):
        return f"Avtomabil modeli:{self.model}, rangi:{self.rang}, narxi:{self.narx}, yil:{self.yil}, probegi:{self.kilometr}"
    def update_km(self,kilometr):
        if kilometr >= self.kilometr:
            self.kilometr=kilometr
        else:
            print("Xato: kilometrni ozgartrib bolmaydi")
a1 = Auto('Malibu', 'qora', 'avtomat', 390000000, 2023, 10000)
print(f"Avtomobil modeli: {a1.model}, rangi:{a1.rang}, narxi:{a1.narx}, yili:{a1.yil}, probegi:{a1.kilometr}")
a2=Auto('Gentra','Oq','avtomat',200000000,2024,5000)
print(f"Avtomobil modeli: {a2.model}, rangi: {a2.rang}, narxi: {a2.narx}, yili:{a2.yil}, probegi:{a2.kilometr}")
a1.update_km(11000)
print(a1.get_info())


#2 Avtosalon klasi
class Autosalon:
    def __init__(self,nomi,manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.autolar=[]
    def add_auto(self,auto):
        self.autolar.append(auto)
    def show_autolar(self):
        print(f"{self.nomi} avtosaloni ({self.manzili}) dagi avtomobillar")
        for auto in self.autolar:
            print(auto.get_info())
salon=Autosalon("GM Uzbekiston","Asaka")
salon.add_auto(a1)
salon.add_auto(a2)
salon.show_autolar()
print(dir(Auto))
print(Auto.__dict__)
