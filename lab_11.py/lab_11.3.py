a = [i ** 4 for i in range(0,4)]

print(a)

for i in a:
    print(i)

iterator = iter(a)

print("первый элемент списка - ", next(iterator))
print("слудующий элемент списка - ", next(iterator))
print("слудующий элемент списка - ", next(iterator))
print("слудующий элемент списка - ", next(iterator))

