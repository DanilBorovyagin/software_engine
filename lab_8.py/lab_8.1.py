
class Mobil:  # создаём класс Mobil
    def __init__(self, make, model):  # создаём функцию, инициализируем новый объект
        self.make = make  # обращение к атрибуту make
        self.model = model  # обращение к атрибуту model

    def __str__(self):  # определяет строкове значение в классе Mobil
        # возвращает строку соджащую строкове значение атрибутов make и model
        return f"производитель = {self.make}, модель = {self.model}"


my_mobil = Mobil("Samsung", "s10e")
print(my_mobil)
