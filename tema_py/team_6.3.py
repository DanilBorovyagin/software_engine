from collections import Counter
user = input("число: ")


def rid(users):
    counter = Counter(users)
    most = counter.most_common(3)
    most_sort = sorted(most, key=lambda x: x[1])
    res = {int(num): count for num, count in most_sort}
    return res


user_most = rid(user)
print(user_most)