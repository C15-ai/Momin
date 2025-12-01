#1


#def tugilgan_yil(name):
    #ism=input("ismingizni kriting>>")
    #yosh=int(input("yoshingizni  kriting>>"))
    #yil= 2025 - yosh
    #print(f"{ism}, siz {yil}-yilda tugulgansiz")
#tugilgan_yil("Momin")

#2
#def kvadrad_kub(son):
    #son=int(input("Son kriting>>>"))
    #print(f"Sonning kvadradi : {son**2}")
    #print(f"Sonning kubi :{son**3}")
#kvadrad_kub(3)

#3
#def juft_toqligi(son):
    #son=int(input("Son kriting>>>"))
    #if son %2==0:
        #print("Juft son")
    #else:
        #print("Toq son")
#juft_toqligi(3)

#4
#def katta_sonni_cqar(son):
    #a=int(input("1-sonni kriting>>"))
    #b=int(input("2-sonni kriting>>"))
    #if a>b:
        #print(f"katta son {a}")
    #elif b>a:
        #print(f"katta son {b}")
    #else:
        #print(f"sonlar teng")
#katta_sonni_cqar(2)

#5
#def darajani_cqar(x,y=2):
    #result=x**y
    #print(f"{x}**{y} = {result}")
#darajani_cqar(3)

#6
#def bolinishlarni_cqar(son):
    #for i in range (2,11):
        #if son % i == 0 :
            #print(f"{son} {i} ga qoldiqsiz bolinadi")
#bolinishlarni_cqar(16)


#-----------------------------------------------------------------------------------------------------------------------


#1
#def f_malumoti(name):
    #ism=input("Ism kriting>>>")
    #familiya=input("Familiya kriting>>>")
    #tugulgan_yili=input("Tugilgan yilini kriting>>>")
    #tugulgan_joyi=input("Joy kriting>>>")
    #email=input("Email kriting>>>")
    #raqam=int(input("raqam kriting>>>"))
    #yosh= input("yosh kriting>>>")
    #malumot={
        #"ism":ism,
        #"familiya":familiya,
        #"yil":tugulgan_yili,
        #"joy":tugulgan_joyi,
        #"raqam":raqam,
        #"yosh":yosh,
#}
    #return malumot
#f_malumoti("Momin")


#2
#mijozlar=[]
#def mijozlar_royxati(name):

       #while True:
        #mijozlar.append(malumot())
         #davom_etasmi=input("Yana mijoz qoshasizmi(ha/yoq)>>")
         #if davom_etasmi!=hash
             #break
           #print("Mijozlar royhati")
             #for i in mijozlar
                #print(f"{i['ism']} {i['familiya']} {i[yosh]}")
#mijozlar_royxati("Momin")


#4
r=int(input("radiusni kriting>>"))

def aylana_info(r):

    d=r*2
    p=r*3.14
    y=(r*3.14)*2
    a={

        "radiusi":r,
        "diametri":d,
        "peremetri":p,
        "yuza":y,
    }
    return a

print(aylana_info(r))













