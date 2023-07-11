
class Student:

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def muskan(self):
        print(f"name is {self.name}, age is {self.age} and salary is {self.salary}")

    def __add__(self, other):
        return self.salary+ other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __repr__(self):
        return f"Here the details of the student ..name = {self.name} , age= {self.age} and salary is {self.salary}"

    def __str__(self):
       return f"name is {self.name}, age is {self.age} and salary is {self.salary}"

obj=Student("Muskan",19,92871)
obj1=Student("sehaj",12,768)

print(obj//obj1)
# print(obj.__repr__())
print(obj.__str__())
print(repr(obj))
print(obj)


