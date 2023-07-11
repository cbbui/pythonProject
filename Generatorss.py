

# def muskan(n):
#
#     for i in range(n):
#         yield i
#
#
# g=muskan(4)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())



def table(n):
    for i in range(1,11):
        n*i
        i=i+1
        yield i

    for j in i:
        print(j)

a=table(6)
print(a)