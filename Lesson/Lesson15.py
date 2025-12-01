#nom, narxi, soni = 'adrenaline', 200, 20


#products = {
 #   'adrenaline': {'narxi': 200, 'soni': 20},
  #  'coca-cola': {'narxi': 10000, 'soni': 30},
   # 'morojniy': {'narxi': 20000, 'soni': 10},
    #'non': {'narxi': 5000, 'soni': 200}
#}

#jami=0
#for k,v in products.items():
 #   jami=soni *narxi
  #  products[k]['jami']=jami
#print(products)

#nomsiz funksiyalar

#summa = lambda x, y: x + y
#print(summa(12,14))

#from math import sqrt
#sonlar = list(range(1,11))



#sonlar=list(range(1,10))
#empty=[]
#print(sonlar)
#for i in sonlar:
    #empty.append(i**2)
#print(empty)

#kv_sonlar=list(map(lambda x:x**2,sonlar))
#print(kv_sonlar)



#matn='salom123'
#result=list(map(lambda x:x.isalpha(),matn ))
#print(result)

#import random as r
#sonlar=r.sample(range(10000000000000),(1000))
#print(sonlar)

#juft_sonalr =list(filter(lambda x : x%2==0, sonlar))
#print(juft_sonalr)
#print(sonlar)
#print(len(juft_sonalr)//len(sonlar))


#3number=int(input('son kriting>>>'))
#result=1
#while number!=0:
    #result*=number
    #number-=number
#print(result)

#def factorial(number):
    #if number==1:
        #return 1
    #else:
        #return number+factorial(number-1)
#print(factorial(3))


#def sana(n):
    #print(n)
    #if n==1:
        #return

    #sana(n-1)
#sana(5)




#def n_sonlar(n):
    #print(n)
    #if n==1:
        #return
    #else:
        #return n+n_sonlar(n-1)
#n_sonlar(5)


#dict
#1️⃣ Boshlang‘ich ma’lumot (tayyor dict)
   #```python
students = {
       "student1": {"name": "Ali", "age": 20, "grade": "B"},
       "student2": {"name": "Laylo", "age": 22, "grade": "A"},
       "student3": {"name": "Sardor", "age": 19, "grade": "C"}
}
students["student1"]["grade"] = "A+"
#print(students)

students["student3"].update({"City":"Tashkent"})
#print(students)

students["student4"]={"name": "Bob", "age": 20, "grade":"A", "city":"Tashkent"}
#print(students)

for key,info in students.items():
    name=info.get("name")
    age=info.get("age")
    grade=info.get("grade")
    city=info.get("city","Tashkent")
    print(f"Student:{name},age:{age} grade:{grade},city:{city}")

students["student1"].update({"grade":"A","city":"Navoiy"})
#print(students)

#print("Oldingi holat")
print({
    "student1": {"name": "Ali", "age": 20, "grade": "B"},
    "student2": {"name": "Laylo", "age": 22, "grade": "A"},
    "student3": {"name": "Sardor", "age": 19, "grade": "C"}
})
print("YAngi holat")
print(students)





#   }
#2️⃣ Bitta elementni yangilash
#• "student2" ichidagi "grade" qiymatini "A+" ga o‘zgartiring.
#• .update() yoki to‘g‘ridan-to‘g‘ri students["student2"]["grade"] = "A+" usulidan foydalaning.

#3️⃣ Yangi kalit qo‘shish (nested darajada)
#• "student3" ichiga "city": "Tashkent" nomli yangi juftlik qo‘shing.
#• .update() metodidan foydalaning.

#4️⃣ Yangi talaba qo‘shish (tashqi darajada)
#• "student4" nomli yangi kalit yarating, qiymati dictionary bo‘lsin:
#python {"name": "Malika", "age": 21, "grade": "B", "city": "Fergana"}

#5️⃣ Ma’lumotni chiqarish
#• Hamma talabalarni for sikl orqali chiqaring:
#Talaba: Ali, Yosh: 20, Bahosi: B ...

#6️⃣ .update() orqali bir nechta qiymatni bir vaqtning o‘zida yangilash
#• "student1" uchun: {"grade": "A", "city": "Andijan"} ni .update() bilan yangilang.

#7️⃣ O‘zgartirishdan oldingi va keyingi holatni solishtiring.
#• Yangilanishdan oldin va keyin print(students) qilib farqni ko‘ring.
