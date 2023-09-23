one = int(input("введите число"))

if one < 0:
    print("число меньше 0")

elif 0 < one < 10:
    print("число больше 0 и меньше 10")

elif one > 10:
    print("число больше 10")
else:
    print("число равно 10")