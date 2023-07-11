
class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age


    def muskan(self):

         return f"name is {self.name} and the age is {self.age}"

obj=Student("Muskan",19)
print(obj.muskan())

print(type(obj))
print(id(obj))
print(dir(obj))

import inspect

print(inspect.getmembers(obj))

