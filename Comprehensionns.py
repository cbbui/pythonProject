


# l1=[]
# for i in range(100):
#     if i%2==0:
#         l1.append(i)
#
# print(l1)


# LIST COMPREHENSIONS
l1=[i for i in range(100) if i%2==0]
print(l1)

# DICTIONARY COMPREHENSIONS

d1={ i:f"Item{i}" for i in range(101)}
print(d1)

d2={value:key for key,value in d1.items()}
print(d2)

# SET COMPREHENSIONS

s={dress for dress in ["dress 1","dress 2","dress 3","dress 2","dress 2","dress 2",]}

print(s)

# GENERATOR COMPREHENSIONS

muskan=(i for i in range(1000))
# print(muskan.__next__())
# print(muskan.__next__())

for a in muskan:
    print(a)














