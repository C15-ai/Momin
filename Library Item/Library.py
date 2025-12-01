class Shaxs:
    def __init__ (self,ism,familiya,yosh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.yosh} yoshda"
class Talaba(Shaxs):
     def __init__ (self,ism,familiya,yosh,id_raqam):
         super().__init__ (ism,familiya,yosh)
         self.id_raqam = id_raqam
         self.fanlar=[]
     def fanga_yozil(self,fan):
         self.fanlar.append(fan)
         print(f"{self.ism} {fan.nomi}  faniga yozildi")

     def remove_fan(self, fan):
         if fan in self.fanlar:
             self.fanlar.remove(fan)
             print(f"{fan.nomi} fani o‘chirildi.")
         else:
             print("Bu fanga yozilmagan.")
     def get_info(self):
         fan_nomlari=[fan.nomi for fan in self.fanlar]
         return f"Talaba: {self.ism} {self.familiya}, ID: {self.id_raqam}, Fan: {fan_nomlari}"
class Fan:
    def __init__ (self,nomi):
        self.nomi = nomi
    def get_info(self):
        return f"Fan: {self.nomi}"
class Professor(Shaxs):
    def __init__ (self,ism,familiya,yosh,kafedra):
        super().__init__(ism,familiya,yosh)
        self.kafedra = kafedra
    def get_info(self):
        return f"Professor {self.ism} {self.familiya}  {self.kafedra} kafedrasi"
class Foydalanuvci(Shaxs):
    def __init__ (self,ism,familiya,yosh,login):
        super().__init__(ism,familiya,yosh)
        self.login = login
    def get_info(self):
        return f"Foydalanuvci: {self.ism} ({self.login})"
class Admin(Foydalanuvci):
    def __init__ (self,ism,familiya,yosh,login):
        super().__init__(ism,familiya,yosh,login)
    def get_info(self):
        return f"Admin {self.ism} {self.familiya},foydalanish logini:{self.login}"
    def ban_user(self,foydalanuvci):
        print(f"Foydalanuvci: {foydalanuvci.login} bloklandi")

matematika=Fan("Matematika")
fizika=Fan("Fizika")
tarix=Fan("Tarix")

t1=Talaba('Ali','Asomov',20 ,'T1111')

t1.fanga_yozil(matematika)
t1.fanga_yozil(fizika)

print(t1.get_info())
t1.remove_fan(tarix)
t1.remove_fan(matematika)
p1=Professor("Anvar","Saidov",45,"Avtomatlashtrish")
print(p1.get_info())
a1=Admin("Momin","Tursunov",18,"t1t1t1t1t1tt1")
f1=Foydalanuvci("Ali","Gaybulayev",21,"tftxjtyc1222")
a1.ban_user(f1)
print(a1.get_info())