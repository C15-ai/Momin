# sonlar = [1,2,3,4,5]
# for i in sonlar:
#     print(i)
#
# class Students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age =age
#
# class University:
#     def __init__(self,name,location):
#         self.name = name
#         self.location = location
#         self.students = []
#     def __iter__(self):
#         return iter(self.students)
#     def __next__(self):
#         pass
# s1 = Students("Ali",19)
# s2 = Students("Vali",20)
# u1 = University("TKTI","NAVOIY")
# u1.students = [s1,s2]
# for i in u1:
#     print(i.name)
# class MyIterator:
#     def __init__(self,start,end):
#         self.current = start
#         self.end = end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         self.current += 1
#         return self.current - 1
#
#
# for i in MyIterator(1,6):
#     print(i)
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
def xrange(n):
    return range(n)
a = yrange(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# for i in a:
#     print(a)