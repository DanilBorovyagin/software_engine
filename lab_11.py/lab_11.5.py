def count(con):
    while con <= 100:
        yield con
        con += 1


counter = count(10)
for i in counter:
    print(i)
