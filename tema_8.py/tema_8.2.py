rol = input("введите роль: ")
drawing = input("ближний бой или дальний бой ")
champions = input("Введите чампиона: ")


class Lol:
    def __init__(self, role, draw, champ):
        self.role = role
        self.draw = draw
        self.champ = champ

    def play(self):
        print(f"ваша роль:{self.role} ваш чампион:{self.champ} дальность атаки вашего чампиона:{self.draw}")

    def get_info(self):
        print(f"роль: {self.role}\nчемпион: {self.champ}\nдальность атаки: {self.draw}")

    def is_mage(self):
        mages = ["аурелион сол", "вейгар", "зиггс"]
        if self.champ in mages:
            return print("чемпион является магом")
        else:
            return print("чампион не является магом")


my_lol = Lol(rol, drawing, champions)
my_lol.get_info()
my_lol.play()
my_lol.is_mage()
