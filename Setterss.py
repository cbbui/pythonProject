

class Student:

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    @property
    def email(self):
        if self.fname=="none" and self.lname=="none":
            return "There is no email.Set it using setters"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,a):
        names=a.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname="none"
        self.lname="none"



obj=Student("Muskan","Kaur")
print(obj.email)

obj.fname="Sehaj"
print(obj.email)

obj.lname="singh"
print(obj.email)



obj.fname="Sehaj"
print(obj.fname)


obj.email="this.that@gmail.com"
print(obj.email)
print(obj.fname)
print(obj.lname)


del obj.email
print(obj.email)


#
# class Student:
#
#     def __init__(self,s1,marks):
#         self.s1=s1
#         self.marks=marks
#
#     def printDetails(self):
#         return f"{self.s1}  {self.marks}"
#
#
# object=Student("Muskan",200)
# object1=Student("Sehaj",322)
# print(object.printDetails())
#
# object.marks=350
# print(object.printDetails())
#
# object.s1="pawan"
# print(object.printDetails())
