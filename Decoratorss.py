

def dec(f1):
    def a():
        print("hello")
        f1()
        print("byee")
    return  a

@dec
def muskan():
    print("My name is muskan kaur")


# muskan=dec(muskan)
muskan()







