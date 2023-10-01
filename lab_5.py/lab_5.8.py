from random import *


def list():
    f = [randint(4,444)] * randint(4,44)
    return f


res = []
for i in range(randint(1,4)):
    res.append(list())

    print(res)