list_2= (5,5,3,1,9)
list_1= (5,5,3,"1",9)
tup_2 = tuple(list_2)
tup_1 = tuple(list_1)

if not isinstance(tup_1, int):
    print(list_1)
else:
    print(sorted(tup_1))

if not isinstance(tup_2, int):
    print(list_2)
else:
    print(sorted(tup_2))