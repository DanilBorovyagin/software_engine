import random


def roll_dice():

    kub = random.randint(1, 6)
    print("На кубике выпало", kub)

    if kub == 5 or kub == 6:
        print("Вы победили")
    elif kub == 3 or kub == 4:
        print("Ничего не произошло. Бросаем кубик снова...")
        roll_dice()
    else:
        print("Вы проиграли")


if __name__ == "__main__":
    roll_dice()
