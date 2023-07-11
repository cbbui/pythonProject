
# METHOD

class Employee:



   def muskan(self):
      return f"The name is {self.name} , salary is {self.salary}, empid is {self.empid}"


obj1=Employee()
obj2=Employee()

obj1.name="muskan"
obj1.salary=100000
obj1.empid=2729

obj2.name="sehaj"
obj2.salary=10
obj2.empid=8796

print(obj2.muskan())



# USING CONSTRUCTOR INIT

class Employee:

      def __init__(self, aname, asalary, aempid):
          self.name=aname
          self.salary=asalary
          self.empid=aempid




obj1 = Employee("Muskan", 100000, 2729)
obj2 = Employee("sehaj", 199223, 1987)


print(obj2.name)


