from collections import *


def long(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read().split()
        count = Counter(content)
        longer_max = len(max(count, key=len))
        longer = [word for word in count if len(word) == longer_max]
        return longer


print(long("need.txt"))