

class A:
    x="I am x in class A"

    def __init__(self):
        # self.x="I am x in constt init"
        self.muskan="I am muskan in constt init in A"
        self.sehaj = "I am sehaj in constt init in A"


class B(A):
    x = "I am x in class B"

    def __init__(self):
         # self.muskan="I am muskan in constt init in B"
         super().__init__()
         self.sehaj = "I am sehaj in constt init in B"
         self.harry="I am harry in constt init in B"




a=A()
b=B()

print(b.x)
print(b.muskan)
print(b.sehaj)




