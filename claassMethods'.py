
class Employee:
      holidays=29



      @classmethod
      def change_holidays(cls,newholi):
          cls.holidays=newholi

Employee.change_holidays(45)
print(Employee.holidays)