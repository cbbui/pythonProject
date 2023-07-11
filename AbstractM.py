from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        return 0

class rectangle(shape):

    def __init__(self):
        self.length=6
        self.bredth=7

    def area(self):
        print("area of the rectangle is: ")
        return self.length*self.bredth


class square(shape):

    def __init__(self):
        self.a=10

    def area(self):
        print("area of the square is: ")
        return self.a*self.a

obj2=square()
obj1=rectangle()

print(obj1.area())
print(obj2.area())
