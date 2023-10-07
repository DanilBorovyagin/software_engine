def info (name, age, status, company="нет названия",):
    print(f"имя:{name} возвраст:{age} компания: {company} статус:{status} ")


dan = ("Данил", 21, "стажёр","google", )
info(*dan)

jin =("Андрей", 30, "работает","google", )
info(*jin)

jini =("Андрей", 30, "работает")
info(*jini)