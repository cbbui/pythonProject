
# m=1
# n=18
# while(m<5):
#
#     a=int(input("Write your number"))
#     print("number of guesses left", 5 - m)
#
#     if a<n:
#         print("choose greater number")
#
#         continue
#
#     elif a>n:
#         print("choose smaller number")
#
#         continue
#
#
#     elif a==n:
#         print("wuhoo! you choose right number")
#
#         break
#
#     else:
#         print("choose right number ")
#
#         # print("number of guesses i took to finish ",m)
#
#
#
# if m>5:
#     print("Game over")
# m=m+1

# print("pattern")
# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#
#     print("")

# a=int(input("enter number "))
# i=1
# sum = 0
# for i in range(1,a+1,1):
#
#
#
#     sum=sum+i
# print("sum")
# print(sum)


# a=int(input("write a number whose table you wanna print\n"))
#
# for i in range(0,12):
#     print(a," * ",i," = ",a*i)

# l1=["muskan","sukuna","sehaj","harry","eren","levi","itadori"]

# for i in l1:
#     print(i)


a=4
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end=" ")
    print()


a=4
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()