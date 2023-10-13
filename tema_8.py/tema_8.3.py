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
my_lol.play()
my_lol.is_mage()


class ATK(Lol):
    def __init__(self, role, draw, champ, ad, ap):
        super().__init__(role, draw, champ)
        self.ad = ad
        self.ap = ap

    def TXT_ATK(self):
        print(f"роль: {self.role}\nчемпион: {self.champ}\nдальность атаки: {self.draw}\nад урон: {self.ad}\nап урон: {self.ap}")

    def is_ATK(self):
        ap_champ = ["аурелион сол", "вейгар", "зиггс"]
        if self.champ in ap_champ:
            return print(f"урон ап {self.ap}")
        else:
            return print(f"урон ад {self.ad}")


my_ATK = ATK(rol, drawing, champions, 130, 240)
my_ATK.TXT_ATK()
my_ATK.is_ATK()
