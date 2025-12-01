# Context Meneger
# class MyContextManager:
#     def __enter__(self):
#         return "Bu resurs"
#
#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print("Konteksdan Ciqyapmiz")
#         if exc_type:
#             print("Istisno qilyamiz")
#         return True
# with MyContextManager() as context:
#     print(f"resurs{context}")
#     raise ValueError("Bu test istisno")
from fileinput import filename

# class File:
#     def __init__(self, filename,mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file :
#             self.file.close()
# with File("test.txt","w") as f:
#     f.write("hello world")

filename = "example.txt"
data = "hello world"
file = None
try:
    file = open(filename, "w")

    file.write(data)
except ValueError:
    pass
finally:
    if file:
        file.close()
