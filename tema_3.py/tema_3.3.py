i = int(input("Введите число от 1 до 10:"))

if 0 < i < 11:
        if i <= 3:
            print("от 0 до 3 включительно")
        elif 3 < i < 6:
            print("от 3 до 6")
        elif 6 < i <= 10:
            print("от 6 до 10 включительно")

else:
    print("число выходит за диапозон допустимых")
