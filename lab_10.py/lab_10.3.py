def check(func):
    def out(*args):
        name, age = args[0], args[1]

        if age < 0 or age > 100:
            age = "недопустимы вовраст "
        func(name, age)

    return out


def data(*args):
    try:
        for i in range(len(*args)):
            try:
                res = (args[0][i] * 15) // 10
                print(res)
            except Exception as ex:
                print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print("вся информация обработана")


@check
def person(name, age):
    print(f"имя: {name} возраст: {age}")


person('Владимир', 38)
person("Александр", -5)
person('Петр', 138, 15, 48, 2)

data([1, 15, "hell", 'Hello', 'i', 'try', 'to', 'crash', 'your', 'site', 38, 45])
