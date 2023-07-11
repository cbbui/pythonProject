

class Employee:
    holidays=10
    pass

obj1=Employee()
obj2=Employee()

obj1.name="muskan"
obj1.salary=100000
obj1.empid=2729

obj2.name="sehaj"
obj2.salary=10
obj2.empid=8796

print(obj1.name,obj1.empid,obj1.salary)
print(obj2.name,obj2.empid,obj2.salary)
print(obj1.holidays)

Employee.holidays=12

print(obj1.holidays)
print(Employee.holidays)

print(obj1.__dict__)
print(obj2.__dict__)
















