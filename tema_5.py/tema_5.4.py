one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
four = 4
vi = [2]

updete_1 = [four if i == 3 else i for i in one]
updete_2 = [four if i == 3 else i for i in two]
updete_3 = [four if i == 3 else i for i in three]

for d in vi:
    while d in updete_1:
        updete_1.remove(d)

for d in vi:
    while d in updete_2:
        updete_2.remove(d)

for d in vi:
    while d in updete_3:
        updete_3.remove(d)
print(updete_1)
print(updete_2)
print(updete_3)