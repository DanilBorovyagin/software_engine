class check:
    def __init__(self, func):
        print("> класс check метод __init__ успешный запуск")
        self.func = func

    def __call__(self):
        print("> проверка перед запуском", self.func.__name__)
        self.func()
        print("> Проверка безопасного подключения")


@check
def site():
    print("сайт работает")


print(">> сайт запущен")
site()
print(">> сайт выключен")
