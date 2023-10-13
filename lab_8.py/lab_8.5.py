class Shape:  # создаём родительский класс
    def area(self):  # пустой метод area
        pass


class Kva(Shape):  # создаём наследственный класс
    def __init__(self, a, b):  # инициализируем атрибуты
        self.a = a  # обращение к атрибуту
        self.b = b  # обращение к атрибуту

    def area(self):  # инициализируем метод
        return self.a * self.b  # Возвращаем площадь прямоугольника


class Cir(Shape):  # создаём наследственный класс
    def __init__(self, r):  # инициализируем атрибуты
        self.r = r  # обращение к атрибуту

    def area(self):  # инициализируем метод
        return 3.14 * self.r * self.r  # Возвращаем площадь круга


shapes = [Kva(5, 5), Cir(3)]  # Создаем список объектов разных фигур
for Shape in shapes:
    print(Shape.area())  # Выводим площадь каждой фигуры
