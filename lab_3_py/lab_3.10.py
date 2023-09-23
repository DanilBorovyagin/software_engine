massiv = [7, 43, 433, 4443, 41]
flag = False
for i in massiv:
    if i % 2 == 0:
        flag = True

if flag is True:
    print("есть чётное число")
else:
    print("нет чётного числа ")