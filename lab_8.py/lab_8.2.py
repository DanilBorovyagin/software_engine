class Mobil:  # создаём класс Mobil
    def __init__(self, make, model):  # создаём функцию, инициализируем новый объект
        self.make = make  # обращение к атрибуту make
        self.model = model  # обращение к атрибуту model

    def us(self):  # создаём функцию для вывода значений атрибутов на экран
        print(f"use my smartphone company {self.make} models {self.model}")  # выводим значения на экран


my_mobil = Mobil("samsung", "S10")  # задаём значения для атрибутов
my_mobil.us()  # вызываем функцию us для вывода в консоль
