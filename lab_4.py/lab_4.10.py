global result


def prim():
    a = int(input("Ширина "))
    b = int(input("Высота "))
    global result
    result = a * b


def tria():
    a = int(input("Длинна основания"))
    h = int(input("Высота"))
    global result
    result = (a*h)/2


fi = input("1 - прямоугольник, 2 - треугольник: ")

if fi == "1":
    prim()
elif fi == "2":
    tria()

print(f"Площадь фигуры: {result}")
