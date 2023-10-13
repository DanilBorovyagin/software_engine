class Mobil:  # создаём класс Mobil
    def __init__(self, make, model):  # создаём функцию, инициализируем новый объект
        self._make = make  # обращение к защищённому атрибуту make
        self.__model = model  # обращение к приваиному атрибуту model

    def __str__(self):  # определяет строкове значение в классе Mobil
        # возвращает строку соджащую строкове значение атрибутов make и model
        return f"производитель = {self._make}, модель = {self.__model}"

    def us(self):  # создаём функцию для вывода значений атрибутов на экран
        print(f"use my smartphone company {self._make} models {self.__model}")  # выводим значения на экран


my_mobil = Mobil("Samsung", "S10e")
print(my_mobil._make)  # доступ к защищёному атрибуту
my_mobil.us()  # вызов метода
