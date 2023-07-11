
# MAP
l=["2","34","25","9","2","67"]


for i in range(len(l)):
    l[i]=int(l[i])

l[3]=l[3]+4
print(l[3])

l=list(map(int,l))

l[4]=l[4]+10

print(l[4])


# FILTER


l=[3,4,5,6,7,7,8,9]
def f1(a):
    return a>5


m=list(filter(f1,l))
print(m)

# REDUCE

from functools import reduce

list=[2,3,4,5,6,9,3]

n=reduce(lambda x,y:x+y ,list)
print(n)
