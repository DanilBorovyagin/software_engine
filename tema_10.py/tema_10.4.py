def area_decorator(func):
    def wrapper(*args, **kwargs):  # функция принимает любое количество аргументов
        print("Вычисление площади начато...")  # выводим надпись
        result = func(*args, **kwargs)  # вызов оригинальной функции
        print("Вычисление площади завершено.")  # выводим надпись
        return result  # возвращаем значение
    return wrapper  # возвращаем значение


@area_decorator
def rectangle_area(length, width):  # функция для рассчёта площади
    return length * width  # формула для подсчёта


@area_decorator
def circle_area(radius):  # функция для рассчёта площади
    return 3.14 * radius**2  # формула для подсчёта


def main():  # для выбора действия и ввода даных пользователем
    print("Выберите фигуру:")  # выводим надпись
    print("1. Прямоугольник")  # выводим надпись
    print("2. Круг")  # выводим надпись
    choice = input("Введите номер фигуры (1-2): ")  # выводим надпись

    if choice == "1":
        length = float(input("Введите длину прямоугольника: "))  # ввод данных
        width = float(input("Введите ширину прямоугольника: "))  # ввод данных
        area = rectangle_area(length, width)  # передаём данные в функцию
        print("Площадь прямоугольника:", area)  # выводим надпись с площадью

    elif choice == "2":
        radius = float(input("Введите радиус круга: "))  # ввод данных
        area = circle_area(radius)  # передаём данные в функцию
        print("Площадь круга:", area)  # выводим надпись с площадью

    else:
        print("Неверный выбор.")  # выводим надпись


main()  # вызываем функцию
