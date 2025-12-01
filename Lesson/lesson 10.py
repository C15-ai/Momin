#1
#import random

#comp_number =random.randint(1,10)

#son =int(input("Komp son oylaydi siz taxmin qling>>"))

#guess = 1
#while comp_number != son:
    #if comp_number > son:
        #son = int(input("Kattaroq son tahmin qling>>"))
    #else:
        #son = int(input("kicikroq son tahmin qling>>"))
    #guess += 1

#print(f'Togri son krintingiz,{guess} urunishda')

#2
#import random
#son=int(input("Siz son oylang(1-10)>>"))
#comp_number = random.randint(1,10)
#guess=1
#while comp_number != son:
    #comp_number = random.randint(1,10)
    #guess+=1
#print(f"Togri son topdingiz{guess}urunishda")


#3
#while True:
    #ism = input('ism kiriting>>>')
    #raqam = input('tel raqam kiritng>>>')
    #phone[ism] = raqam

    #answer = input('davom etamizmi?(ha,yoq)')
    #if answer.lower() == 'yoq':
        #break
#print(phone)

#4
goal=10000
kun=0
while goal>=0: 
    qadam=int(input(f"{kun+1} -kun yurgan qadamingizni kriting>>"))
    goal-=qadam
    kun+=1
print(f'Siz 10000 qadamlik maqsadingizni {kun} kunda bajardingiz')


