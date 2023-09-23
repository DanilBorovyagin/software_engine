string = "нет в массиве"
val = [2, 5, 6, 8, 11]
con = 0
while "есть в массиве" not in string:
    memo = string
    if con in val:
        string = "есть в массиве"
    print(string)
    if con < 10:
        string = memo
    con += 1
