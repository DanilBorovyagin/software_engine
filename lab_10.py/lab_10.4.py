class Negativ(Exception):
    pass


def check(name):
    if len(name) > 10:
        raise Negativ("длинна более 10 символов")
    else:
        print("успешная регестрация")


name_two = "вольын"
check(name_two)
name_one = "вольгортонирын"
check(name_one)

