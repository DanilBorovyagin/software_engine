class Animal:
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        return "мяу"


class Dog(Animal):
    def sound(self):
        return "гав"


class Cow(Animal):
    def sound(self):
        return "му"


class Pig(Animal):
    def sound(self):
        return "хрю"


animals = [Cat(), Dog(), Cow(), Pig()]
for Animal in animals:
    print(Animal.sound())