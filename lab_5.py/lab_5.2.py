a = set("asdfgh")
print(a)
for i in range(5):
    a.add(i)
print(a)

b = frozenset("asdfgh")
print(b)
for s in range(5):
    b.add(s)
print(b)