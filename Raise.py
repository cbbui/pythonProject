
#
# a=input("Write your name\n")
# b=input("Write any number\n")
#
#
# if int(b)==0:
#     raise ZeroDivisionError("ZeroDivisionError occur")
#
# if a.isnumeric():
#     raise Exception("Numericals not allowed")
#
# print(f"Hey! {a}")

c=input("Write your name\n")

try:
    print(a)
except Exception as e:

    if c=="Muskan":
        raise ValueError("Muskan is blocked so she's not allowed")

    print("Exception Handled")
    print(e)