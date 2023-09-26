from geron import geron


def user():
    a = float(input("введите длинну стороны a: "))
    b = float(input("введите длинну стороны b: "))
    c = float(input("введите длинну стороны c: "))
    return a, b, c

a, b, c = user()

tria = geron(a, b, c)

print("Площадь ровна: ", tria)