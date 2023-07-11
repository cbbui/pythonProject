import time
from functools import lru_cache

@lru_cache(maxsize=1)
def muskan(n):

    time.sleep(n)
    return n


print("start...")

muskan(4)
print("doing")

muskan(4)

print("still doing..")
muskan(4)

print("done")


