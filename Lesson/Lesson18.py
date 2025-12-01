# class Animal:
# def __init__(self,type,age,):
# self.type = type
# self.age = age
# def get_info(self):
# return f"nomi {self.type}, yoshi {self.age}"


# inheritance

# class People:
#     def __init__(self, name, age, jinsi, cauntry):
#         self.name = name
#         self.age = age
#         self.jinsi = jinsi
#         self.cauntry = cauntry
#     def get_info(self):
#         return f"Ismi {self.name}, yoshi {self.age},jinsi  {self.jinsi},davlati {self.cauntry}"
#
# class Student(People):
#     def __init__(self, name, age, jinsi, cauntry,course,fak):
#          super().__init__(name,age,jinsi,cauntry)
#          self.course = course
#          self.fak = fak
# s1=Student('Ali',18,'m','uz','2',2)
#print(s1.get_info())

#1
class Phone:
    def __init__(self, name,model,color,os):
        self.name = name
        self.model = model
        self.color = color
        self.os = os
class Android(Phone):
    def __init__(self, name,model,color,os,pen):
        super().__init__(name,model,color,os)
        self.pen = pen
class Redmi(Android):
    def __init__(self, name,model,color,os,pen,baterylife):
        super().__init__(name,model,color,os,pen,baterylife)
