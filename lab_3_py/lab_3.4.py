massiv = [-4, -5, 2, 4, 6, 8, 10]

one = int(input("Введите число: "))

if (one in massiv):
    print("Число находится в массиве")

    if one < 0:
        print("Число отрицательное")

    elif one > 0:
        print("число положительное")

    if one % 2 == 0:
        print("Число является четным")

    else:
        print("Число не является четным")

else:
    print(F"числа {one} нет в массиве")