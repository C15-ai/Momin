# class Student:
#     def __init__(self,name,age,university,course):
#         self.name = name
#         self.age = age
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f"Ism:{self.name} {self.age} yoshda {self.university} da  {self.course} kursda oqidi"
# s1 = Student("Juan",18,"TKTI",1)
# # print(s1.get_info())
# s1.age = 20
# s1.course = 2
# print(s1.get_info())
#
#
# class MagistrStudents(Student):
#     def __init__(self,name,age,university,course,prizentation):
#         super().__init__(name,age,university,course,)
#         self.prizentation = prizentation
# m1 = MagistrStudents("Momin",25,"TKTI","Magistr 2","Kutubxona loyihasi")
# print(m1.get_info())


sonlar = [12, 23, 31, 42]
total = 0
for i in sonlar:
     total += i
print(total)
kopaytama = 1
for i in sonlar:
    kopaytama *= i
print(kopaytama)


