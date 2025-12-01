#sklad sistemasi


products={
    'Gorilla':{"Narxi":10000,"Soni":50},
    'Pepsi':{"Narxi":15000,"Soni":100},
    'Snikers':{"Narxi":8000,"Soni":150},
    'Prizidend saryog':{"Narxi":40000,"Soni":80},
}
def mahsulot_qoshish():
    nom = input("Mahsulot nomi: ").strip().lower()
    try:
        narxi = int(input("Narxi (so‘m): "))
        soni = int(input("Soni: "))
        if narxi <= 0 or soni <= 0:
            print(" Narx va son 0 dan katta bo‘lishi kerak!")
            return
    except ValueError:
        print(" Narx va son butun son bo‘lishi kerak!")
        return

    if nom in products:
        products[nom]['soni'] += soni
        print(f" '{nom}' yangilandi. Jami: {products[nom]['soni']} dona.")
    else:
        products[nom] = {'narxi': narxi, 'soni': soni}
        print(f" '{nom}' omborga qo‘shildi.")
#mahsulot_qoshish()

def mahsulot_olish():
    nom = input("Mahsulot nomi: ").strip().lower()
    if nom not in products:
        print(" Mahsulot yoq.")
        return
    try:
        miqdor = int(input("Nechta olasiz "))
        if miqdor <= 0:
            print(" Miqdor 0 dan katta bo‘lishi kerak!")
            return
    except ValueError:
        print(" Miqdor butun son bo‘lishi kerak!")
        return

    available = products[nom]['soni']
    if available < miqdor:
        print(f"️ Zaxira yetarli emas. Mavjud: {available}, so‘rov: {miqdor}")
    else:
        products[nom]['soni'] -= miqdor
        print(f" OK! Qoldi: {products[nom]['soni']} dona.")
#mahsulot_olish()


def mahsulot_royxati():
    print("--------Mahsulotlar royhati--------")
    for nom, info in products.items():
        narxi =info["Narxi"]
        soni = info['Soni']

        print(f"nomi:{nom},narxi:{narxi},soni:{soni}")
#mahsulot_royxati()
def main():
    while True:
        a=int(input(f"1.mahsulot qoshish\n2.mahsulot olish\n3.mahsulot royxati\n0.exit\n nima qilasz"))
        if a ==0:
            break
        elif a==1:
            mahsulot_qoshish()
        elif a==2:
            mahsulot_olish()
        elif a==3:
            mahsulot_royxati()
main()
