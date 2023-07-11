
# SINGLE INHERITENCE

class Employee:
    def a(self):
        return f"name is {self.name}, id is {self.id}, age is {self.age} "

class Programmer(Employee):
    def b(self):
        return f"name is {self.name}, id is {self.id}, age is {self.age} and the salary is {self.salary} "


obj1=Employee()
obj2=Programmer()


obj1.name="Muskan"
obj1.id=2729
obj1.age=19

obj2.name="Muskan"
obj2.id=2729
obj2.age=19
obj2.salary=1000000

print(obj2.a())
print(obj2.b())


# MULTIPLE INHERITENCE

class Employee():
    m=17

    def __init__(self,name,age,salary,id):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id


    def a(self):
        return f"name is {self.name}, age is {self.age}, salary is {self.salary}, id is {self.id} "


class Player():
    m=65

    def __init__(self, name, age, salary, id,gender):

            self.name = name
            self.age = age
            self.salary = salary
            self.id = id
            self.gender=gender

    def b(self):
        return f"name is {self.name}, age is {self.age}, salary is {self.salary}, id is {self.id} and gender is {self.gender} "


class coolHuman(Employee,Player) :
    # m=25

    def __init__(self, name, age, salary, id,gender,language):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
        self.gender = gender
        self.language=language

    def c(self):
          return f"name is {self.name}, age is {self.age}, salary is {self.salary}, id is {self.id} and gender is {self.gender} and language is {self.language} "

    role="all arounder"
    def x(self):
         print(self.role)
         return 2

obj1=Employee("Muskan",19,100000000,2729)
obj2=Player("sehaj",12,18276828,2865,"M")
obj3=coolHuman("pawan",16,10765255,8757,"F","Java")

print(obj3.c())
print(obj3.m)
print(obj3.x())



# MULTILEVEL INHERITENCE

class level1:
    def first(self):
        print('code')


class level2(level1):
    def second(self):
        print('with')


class level3(level2):
    def third(self):
        print('Muskan')


obj = level3()
obj.first()
obj.second()
obj.third()

# DIAMOND PROBLEM IN MULTIPLE INHERITENCE

class A:
    def muskan(self):
        print("Muskan from class A")

class B(A):
    def muskan(self):
        print("Muskan from class B")

class C(A):

    def muskan(self):
        print("Muskan from class C")

class D(B,C):
      def muskan(self):
          print("Muskan from class D")


obj1=A()
obj2=B()
obj3=C()
obj4=D()

print(obj3.muskan())

