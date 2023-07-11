

import time
a=time.time()

i=0
while(i<30):
    print("Muskan")
    i+=1

print("while loop takes time",time.time()-a)
time.sleep(4)

b=time.time()

for j in range(30):
    print("sehaj")

print("for loop takes time\n", time.time() - b)


m=time.asctime(time.localtime(time.time()))
print(m,"\n")


