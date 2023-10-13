class Mobil:  # создаём класс Mobil
    def __init__(self, make, model):  # создаём функцию, инициализируем атрибуты(парметры)
        self.make = make  # обращение к атрибуту make
        self.model = model  # обращение к атрибуту model

    def us(self):  # создаём функцию для вывода значений атрибутов на экран
        print(f"use my smartphone company {self.make} models {self.model}")  # выводим значения на экран


my_mobil = Mobil("samsung", "S10")  # задаём значения для атрибутов
my_mobil.us()  # вызываем функцию us для вывода в консоль


class smartphone(Mobil):  # создание нового класса с указанием родительского
    def __init__(self, make, model, battery):  # создаём функцию, инициализируем атрибуты(параметры)
        super().__init__(make, model)  # вызывает конструктор родительского класса и передаёт ему значение аргументов
        self.battery = battery  # обращение к атрибуту battery

    def charge(self):  # создаём функцию для вывода значений атрибутов на экран
        print(f"Charging the {self.make} {self.model} with {self.battery} kWh")  # выводим значения на экран


my_smartphone = smartphone("Samsung", "S10e", 75)  # задаём значения для атрибутов
my_smartphone.us()  # вызываем функцию us для вывода в консоль
my_smartphone.charge()  # вызываем функцию charge для вывода в консоль
