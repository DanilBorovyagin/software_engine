rol = input("введите роль: ")
drawing = input("ближний бой или дальний бой ")
champions = input("Введите чампиона: ")


class Lol:
    def __init__(self, role, draw, champ):
        self.role = role
        self.draw = draw
        self.champ = champ

    def play(self):
        print(f"ваша роль {self.role} ваш чампион {self.champ} дальность атаки вашего чампиона {self.draw}")


my_lol = Lol(rol, drawing, champions)
my_lol.play()