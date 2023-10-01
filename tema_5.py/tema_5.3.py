from math import *

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

#минимальные значения сторон

one.sort()
two.sort()
three.sort()

a = one[0]
b = two[0]
c = three[0]

#функция подсчёта площади через формулу герона


def tria(a,b,c):
    s = (a + b + c) / 2
    S = sqrt(s * (s - a) * (s - b) * (s - c))
    return S


print(f"сторона а {a} сторона b {b} сторона c {c}")
print("площадь наименьшего треугольника: ",tria(a, b, c))

# Наибольшие значения сторон
one.sort(reverse=True)
two.sort(reverse=True)
three.sort(reverse=True)

a = one[0]
b = two[0]
c = three[0]

print(f"сторона а {a} сторона b {b} сторона c {c}")
print("площадь наибольшего треугольника: ", tria(a, b, c))