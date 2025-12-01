#
#class Student:
    #def __init__(s, name, age,course,university):
        #s.name = name
        #s.age = age
        #s.course = course
        #s.university = university

    #def get_info(s):
        #return f"Talabaning ismi{s.name} ,yoshi {s.age} kursi {s.course} univeri {s.university}"
#s1=Student('Ali',22,2,'TKTI')

#task1


#class User:
    #def __init__(self,name,usernames,email,password):
       #self.name=name
       #self.usernames=usernames
       #self.email=email
       #self.password=password

    #def get_info(self):
        #return f"Foydalanuvchi ismi {self.name} ,usernamemi {self.usernames}, emailmi {self.email}, passwordmi {self.password}"
#u1=User('Momin','m_tursunov','tursunovm545@gmail.com','26022008')
#print(u1.name)
#print(u1.usernames)
#print(u1.email)
#print(u1.password)
#print(u1.get_info())


class University:
    def __init__(self,ism,yosh,grux):
        self.ism=ism
        self.yosh=yosh
        self.grux=grux
class Student(University):
    def __init__(self,ism,yosh,grux,project):
        super().__init__(ism,yosh,grux)
        self.project=project
    def get_info(self):
        return f"Talaba ismi: {self.ism}, Yoshi: {self.yosh} yosh, Gruxi: {self.grux}-grux, Loyixasi:{self.project}"
a1=Student("Momin",18,81,"Library Item")
print(a1.get_info())





