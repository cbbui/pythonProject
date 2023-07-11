
# def a():
#     import time
#     print("Hey there! my name is muskan kaur")
#     time.sleep(5)
#
#     while True:
#         value=(yield)
#         print(value)
#
# s=a()
#
# print("starteddd....")
# next(s)
# print("next method runn")
#
# print("running...")
# print("still running")

#


def a():
    l1=["Muskan","sehaj","harry","harsh","arsh"]

    while True:
        value=(yield )
        if value in l1:
             print(value)
        else:
              print("not found")

cor =a()
print("Write any name")
input()
next()