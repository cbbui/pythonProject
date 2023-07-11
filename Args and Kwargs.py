
# def f1(a,b,c):
#     print(a,b,c)
#
#
# f1("Muskan","sehaj","pawan")

#
# def f1(m,*args):
#     print(m)
#     for b in args:
#         print(b)
#
#
#
# a=["Muskan","sehaj","pawan"]
# m="students are: " \
#   ""
# f1(m,*a)



def f1(m,*args,**kwargs):
    print(m)
    for i in args:
        print(i)
    for j,k in kwargs.items():
        print(j,k)



l1=["Muskan","sehaj","pawan","harry","arsh"]

m="stdents are: "

d={"\nMuskan":"Head","pawan":"monitor","arsh":"sports incharge"}

f1(m,*l1,**d)

