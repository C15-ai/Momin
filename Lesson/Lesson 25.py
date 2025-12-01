#
# a ={
#     "Ali":12,
#     "Vali":22,
#     "Gani":22,
#     "Olim":22
# }
#
#
# with open("about.dat","wb") as f:
#     pickle.dump(a,f)
# import pickle
# class Talaba:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#
#     def __str__(self):
#         return f'Talaba {self.ism} {self.familiya}. Yoshi {self.yosh} da'
#
#
#
#
# t1 = Talaba('Momin', 'Tursunov', 18)
# t2 = Talaba('Chingiz', 'Abdullayev', 18)
# with open("talaba.pickle", "wb") as f:
#     pickle.dump(t1, f)
# with open('talaba.pickle', 'rb') as f:
#     talaba = pickle.load(f)
# print(t1)
# print(t2)

import json
# a = {
#      "Ali":12,
#      "Vali":22,
#      "Gani":22,
#      "Olim":{"ali":21}
# }
# with open('talaba.json','w') as f:
#     json.dump(a,f)
# with open('talaba.json',) as f:
#     talaba = json.load(f)
# print(talaba)
# print(json.dumps(a, indent=4))
# print(type(json.dumps))
import json

with open("talaba.json", 'r') as f:
    data = json.load(f)
data['dorilar'][0]["nomi"] = "Parasetamol"
data['dorilar'][0]["miqdori"] = 1,5
data['dorilar'][1]["nomi"] = "setramon"
data['dorilar'][1]["miqdori"] = 1,5

with open("talaba.json", 'w') as f:
    json.dump(data, f, indent=4)
