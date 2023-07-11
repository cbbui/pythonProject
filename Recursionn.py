# ITERATIVE APPROACH
def f1(n):
    fac=1
    i=0
    for i in range(n):
        fac=fac*(i+1)
    return fac


num=int(input("Enter any number"))
print(f1(num))

# RECURSIVE APPROACH

def f1(n):


    if n==1:
        return 1
    else:
        return n * f1(n-1)



num=int(input("Enter any number\n"))

print(f1(num))