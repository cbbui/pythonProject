
a=input("write 1st number ")
b=input("write 2nd number ")



try:
    print(int(a)+int(b))



except Exception as e:
    print(e)

else:
    print("This will only run when exect doesnt run")

finally:
    print("run me anyhow")



print("done")